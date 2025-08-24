import random
import time
from dataclasses import dataclass
from bisect import bisect_left
from math import exp

# === 사용자의 구현을 import ===
from AVLTree import AVLTree
from Python.tree.BinarySearchTree import BinarySearchTree, BST  # BST만 써도 됨
from RedBlackTree import RedBlackTree


# ===============================
# 1) 메서드 시그니처 차이 흡수 + 루트 갱신 보장
# ===============================
def safe_insert(tree, x):
    try:
        ret = tree.insert(x, tree.root)
        if ret is not None and hasattr(tree, "root"):
            tree.root = ret
        return
    except TypeError:
        pass
    # 3) insert(x, None)
    ret = tree.insert(x, None)
    if ret is not None and hasattr(tree, "root"):
        tree.root = ret

def safe_delete(tree, key):
    # 1) delete(key)
    # 2) delete(key, tree.root)
    try:
        ret = tree.delete(key, tree.root)
        if ret is not None and hasattr(tree, "root"):
            tree.root = ret
        return
    except TypeError:
        pass
    # 3) delete(key, None)
    ret = tree.delete(key, None)
    if ret is not None and hasattr(tree, "root"):
        tree.root = ret

def safe_search(tree, key):
    # search는 반환값의 truthiness만 사용
    try:
        return tree.search(key, tree.root)
    except TypeError:
        return tree.search(key, None)


# ===============================
# 2) 벤치마크 설정/결과
# ===============================
@dataclass
class BenchConfig:
    n_insert: int = 10_000
    n_search_hit: int = 10_000
    n_search_miss: int = 5_000
    n_delete: int = 5_000
    seed: int = 42
    key_range: int = 200_000
    dist: str = "uniform"  # ascending / descending / nearly_sorted / zipf / exp / clustered / uniform

@dataclass
class BenchResult:
    name: str
    t_insert: float
    t_search_hit: float
    t_search_miss: float
    t_delete: float
    total: float


# ===============================
# 3) 치우친 분포 생성 유틸
# ===============================
def make_keys(dist: str, n: int, key_range: int, seed: int = 42, **kw):
    """
    dist:
      - 'ascending'     : 1..n (오름차순 삽입) -> BST 최악
      - 'descending'    : n..1 (내림차순 삽입) -> BST 최악
      - 'nearly_sorted' : 거의 정렬 + 일부만 스왑
      - 'zipf'          : 작은 값 쪽으로 무겁게 (1/x^alpha)
      - 'exp'           : 한쪽 꼬리가 긴 지수분포식 가중
      - 'clustered'     : 몇 개 좁은 구간에 몰림
      - 'uniform'       : 균일 샘플(고유)
    """
    rnd = random.Random(seed)
    if dist == "ascending":
        return list(range(1, n + 1))
    if dist == "descending":
        return list(range(n, 0, -1))
    if dist == "nearly_sorted":
        p = kw.get("p", 0.03)
        arr = list(range(1, n + 1))
        m = max(1, int(n * p))
        for _ in range(m):
            i = rnd.randrange(n); j = rnd.randrange(n)
            arr[i], arr[j] = arr[j], arr[i]
        return arr
    if dist == "zipf":
        alpha = kw.get("alpha", 2.0)
        population = list(range(1, key_range + 1))
        weights = [1.0 / (i ** alpha) for i in population]
        return weighted_unique_sample(population, weights, n, rnd)
    if dist == "exp":
        lam = kw.get("lam", 8.0 / key_range)
        population = list(range(1, key_range + 1))
        weights = [exp(-lam * x) for x in population]
        return weighted_unique_sample(population, weights, n, rnd)
    if dist == "clustered":
        num_clusters = kw.get("num_clusters", 3)
        cluster_width_ratio = kw.get("cluster_width_ratio", 0.005)
        cluster_sizes = cluster_partition(n, num_clusters, rnd)
        res = []
        for size in cluster_sizes:
            center = rnd.randint(int(key_range*0.05), int(key_range*0.95))
            width = max(1, int(key_range * cluster_width_ratio))
            lo = max(1, center - width // 2)
            hi = min(key_range, lo + width)
            block = unique_sample_range(lo, hi, size, seed=rnd.randint(0, 10**9))
            res.extend(block)
        rnd.shuffle(res)
        return res
    # uniform (기본)
    return rnd.sample(range(1, key_range), n)

def weighted_unique_sample(population, weights, k, rnd: random.Random):
    chosen = set()
    res = []
    total = sum(weights)
    cdf = []
    s = 0.0
    for w in weights:
        s += w; cdf.append(s)
    tries = 0
    while len(res) < k:
        tries += 1
        if tries > k * 50:
            remaining = [x for x in population if x not in chosen]
            need = k - len(res)
            res.extend(rnd.sample(remaining, need))
            break
        r = rnd.random() * total
        idx = bisect_left(cdf, r)
        if idx >= len(population):  # 방어
            continue
        v = population[idx]
        if v not in chosen:
            chosen.add(v); res.append(v)
    return res

def cluster_partition(n, groups, rnd: random.Random):
    if groups <= 1: return [n]
    cuts = sorted(rnd.sample(range(1, n), groups - 1))
    parts, prev = [], 0
    for c in cuts:
        parts.append(c - prev); prev = c
    parts.append(n - prev)
    return parts

def unique_sample_range(lo, hi, k, seed=42):
    rnd = random.Random(seed)
    rng = list(range(lo, hi + 1))
    if k >= len(rng):
        rnd.shuffle(rng)
        return rng
    return rnd.sample(rng, k)


# ===============================
# 4) 벤치마크 본체
# ===============================
def benchmark_tree(tree_ctor, name: str, cfg: BenchConfig) -> BenchResult:
    random.seed(cfg.seed)

    # 4-1) 입력 데이터(삽입)
    keys_insert = make_keys(cfg.dist, n=cfg.n_insert, key_range=cfg.key_range, seed=cfg.seed)

    # 4-2) 탐색(hit)은 반드시 삽입된 집합에서 샘플
    if cfg.n_search_hit > len(keys_insert):
        raise ValueError("n_search_hit은 n_insert 이하로 설정하세요.")
    keys_search_hit = random.sample(keys_insert, cfg.n_search_hit)

    # 4-3) 탐색(miss)은 범위 밖에서
    all_candidates = set(range(cfg.key_range, cfg.key_range + cfg.n_search_miss * 10))
    keys_search_miss = random.sample(list(all_candidates), cfg.n_search_miss)

    # 4-4) 삭제도 삽입된 집합에서 샘플
    if cfg.n_delete > len(keys_insert):
        raise ValueError("n_delete는 n_insert 이하로 설정하세요.")
    keys_delete = random.sample(keys_insert, cfg.n_delete)

    # 4-5) 트리 생성
    tree = tree_ctor()

    # 삽입
    t0 = time.perf_counter()
    for x in keys_insert:
        safe_insert(tree, x)
    t_insert = time.perf_counter() - t0

    # 탐색(hit)
    t0 = time.perf_counter()
    hit_cnt = 0
    for key in keys_search_hit:
        if safe_search(tree, key):
            hit_cnt += 1
    t_search_hit = time.perf_counter() - t0

    # 탐색(miss)
    t0 = time.perf_counter()
    miss_cnt = 0
    for key in keys_search_miss:
        if not safe_search(tree, key):
            miss_cnt += 1
    t_search_miss = time.perf_counter() - t0

    # 삭제
    t0 = time.perf_counter()
    for key in keys_delete:
        safe_delete(tree, key)
    t_delete = time.perf_counter() - t0

    total = t_insert + t_search_hit + t_search_miss + t_delete
    # 검증 로그 원하면 주석 해제
    # print(f"[{name}] hit_ok={hit_cnt}/{cfg.n_search_hit}, miss_ok={miss_cnt}/{cfg.n_search_miss}")

    return BenchResult(
        name=name,
        t_insert=t_insert,
        t_search_hit=t_search_hit,
        t_search_miss=t_search_miss,
        t_delete=t_delete,
        total=total,
    )

def pretty_ms(s: float) -> str:
    return f"{s*1000:8.2f} ms"


# ===============================
# 5) 실행부
# ===============================
def main():
    cfg = BenchConfig(
        n_insert=10_000,
        n_search_hit=10_000,
        n_search_miss=5_000,
        n_delete=5_000,
        seed=42,
        key_range=200_000,
        dist="exp",  # 한쪽으로 치우친 입력 기본값
    )

    targets = [
        (AVLTree,      "AVLTree"),
        (RedBlackTree, "RedBlackTree"),
        (BST,          "BinarySearchTree"),
    ]

    results = [benchmark_tree(ctor, name, cfg) for ctor, name in targets]

    print("\n==== Binary Search Tree Benchmark (n≈10k) ====")
    print(f"seed={cfg.seed}, inserts={cfg.n_insert}, search_hit={cfg.n_search_hit}, "
          f"search_miss={cfg.n_search_miss}, delete={cfg.n_delete}, dist={cfg.dist}")
    print("----------------------------------------------")
    header = f"{'Tree':<16} {'Insert':>10} {'Search(hit)':>14} {'Search(miss)':>14} {'Delete':>10} {'Total':>10}"
    print(header)
    print("-" * len(header))
    for r in results:
        print(f"{r.name:<16} "
              f"{pretty_ms(r.t_insert):>10} "
              f"{pretty_ms(r.t_search_hit):>14} "
              f"{pretty_ms(r.t_search_miss):>14} "
              f"{pretty_ms(r.t_delete):>10} "
              f"{pretty_ms(r.total):>10}")
    print("----------------------------------------------")
    winner = min(results, key=lambda x: x.total)
    print(f"Winner: {winner.name} (총 소요시간 기준)")


if __name__ == "__main__":
    import sys
    # ascending/descending에서는 BST 깊이 = n이 될 수 있으므로 넉넉히 올리기
    sys.setrecursionlimit(200_000)
    main()