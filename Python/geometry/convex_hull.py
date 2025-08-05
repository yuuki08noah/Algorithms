from math import atan2


def ccw(p1, p2, p3):
    return (p2[0]-p1[0])*(p3[1]-p1[1]) - (p2[1]-p1[1])*(p3[0]-p1[0])

class ConvexHull:
    def __init__(self, points):
        self.points = points

    def convex_hull(self):
        stack = []
        if len(self.points) < 2:
            return stack

        p0 = min(self.points, key=lambda p: (p[1], p[0]))
        sorted_points = sorted(self.points, key=lambda p: (
            atan2(p[1] - p0[1], p[0] - p0[0]),  # cosθ ≈ x/거리
            (p[0] - p0[0]) ** 2 + (p[1] - p0[1]) ** 2  # 거리 (각도 같을 때 가까운 순)
        ))

        for p in sorted_points:
            while len(stack) >= 2 and ccw(stack[-2], stack[-1], p) <= 0:
                stack.pop()
            stack.append(p)
        return stack

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
convex_hull = ConvexHull(points)
print(len(convex_hull.convex_hull()))
