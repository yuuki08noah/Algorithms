import bisect

class MergeSortTree:
    def __init__(self, arr):
        self.default = 0
        self.length = len(arr)
        self.seg_tree = [0] * (self.length * 4)
        self.arr = arr
        self.build(arr, 1, 0, self.length-1)

    def merge(self, left, right):
        sorted = [0] * (len(left) + len(right))
        mid = (len(left) + len(right)) // 2
        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                sorted[k] = left[i]
                i += 1
            else:
                sorted[k] = right[j]
                j += 1
            k += 1

        for l in range(j, len(right)):
            sorted[k] = right[l]
            k += 1
        for l in range(i, len(left)):
            sorted[k] = left[l]
            k += 1
        return sorted

    def build(self, arr, node, start, end):
        if start == end:
            self.seg_tree[node] = [arr[start]]
            return self.seg_tree[node]
        mid = (start + end) // 2
        self.seg_tree[node] = self.merge(self.build(arr, node * 2, start, mid), self.build(arr, node * 2 + 1, mid + 1, end))
        return self.seg_tree[node]

    def count_less_equal(self, node, start, end, l, r, x):
        if r < start or end < l:
            return 0
        if l <= start and end <= r:
            # x 이하의 수의 개수
            return bisect.bisect_right(self.seg_tree[node], x)
        mid = (start + end) // 2
        return (self.count_less_equal(node*2, start, mid, l, r, x) +
                self.count_less_equal(node*2+1, mid+1, end, l, r, x))

    def count_more(self, node, start, end, l, r, x):
        if r < start or end < l:
            return 0
        if l <= start and end <= r:
            # x 보다 큰 수의 개수
            return len(self.seg_tree[node]) - bisect.bisect_right(self.seg_tree[node], x)
        mid = (start + end) // 2
        return (self.count_more(node*2, start, mid, l, r, x) +
                self.count_more(node*2+1, mid+1, end, l, r, x))

    def kth_smallest(self, l, r, k):
        # 이진탐색 범위는 전체 수열에서 가장 작은 값 ~ 가장 큰 값
        low, high = min(self.arr), max(self.arr)
        answer = -1
        while low <= high:
            mid = (low + high) // 2
            cnt = self.count_less_equal(1, 0, self.length - 1, l, r, mid)
            if cnt >= k:
                answer = mid
                high = mid - 1
            else:
                low = mid + 1
        return answer
