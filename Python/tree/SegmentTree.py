class SegmentTree:
    def __init__(self, arr):
        self.default = 0
        self.length = len(arr)
        self.seg_tree = [0] * (self.length * 4)
        self.build(arr, 1, 1, self.length)
        self.lazy_exist = [False] * (self.length * 4)
        self.lazy_value = [self.default] * (self.length * 4)

    def merge(self, left, right):
        return left + right

    def merge_range(self, value, length):
        return value * length

    def build(self, arr, node, start, end):
        if start == end:
            self.seg_tree[node] = arr[start-1]
            return self.seg_tree[node]
        mid = (start + end) // 2
        left = self.build(arr, node * 2, start, mid)
        right = self.build(arr, node * 2 + 1, mid + 1, end)
        self.seg_tree[node] = self.merge(left, right)
        return self.seg_tree[node]

    def query(self, left, right, node, start, end):
        mid = (start + end) // 2
        if self.lazy_exist[node]:
            self.lazy_exist[node] = False
            self.push_down(self.lazy_value[node], node * 2, start, mid)
            self.push_down(self.lazy_value[node], node * 2 + 1, mid + 1, end)
            self.lazy_value[node] = self.default
        if right < start or left > end:
            return self.default
        if left <= start and right >= end:
            return self.seg_tree[node]

        return self.merge(self.query(left, right, node * 2, start, mid), self.query(left, right, node * 2 + 1, mid + 1, end))

    def update(self, index, value, node, start, end):
        if index < start or end < index:
            return self.seg_tree[node]
        if start == end:
            self.seg_tree[node] = value
            return self.seg_tree[node]
        mid = (start + end) // 2
        left = self.update(index, value, node * 2, start, mid)
        right = self.update(index, value, node * 2 + 1, mid + 1, end)
        self.seg_tree[node] = self.merge(left, right)
        return self.seg_tree[node]

    def update_range(self, left, right, value, node, start, end):
        mid = (start + end) // 2
        if self.lazy_exist[node]:
            self.lazy_exist[node] = False
            self.push_down(self.lazy_value[node], node * 2, start, mid)
            self.push_down(self.lazy_value[node], node * 2 + 1, mid + 1, end)
            self.lazy_value[node] = self.default

        if right < start or end < left:
            return self.seg_tree[node]

        if left <= start and end <= right:
            self.seg_tree[node] = self.merge_range(value, end - start + 1)
            if start != end:
                self.push_down(value, node * 2, start, mid)
                self.push_down(value, node * 2 + 1, mid + 1, end)
            return self.seg_tree[node]

        left_value = self.update_range(left, right, value, node * 2, start, mid)
        right_value = self.update_range(left, right, value, node * 2 + 1, mid + 1, end)
        self.seg_tree[node] = self.merge(left_value, right_value)
        return self.seg_tree[node]

    def push_down(self, value, node, start, end):
        if start == end:
            self.seg_tree[node] = value
            return self.seg_tree[node]

        self.lazy_exist[node] = True
        self.lazy_value[node] = value
        self.seg_tree[node] = self.merge_range(value, end - start + 1)
        return self.seg_tree[node]

    def get_nth_smaller(self, node, start, end, nth):
        if self.seg_tree[node] < nth: return -1
        if start == end: return start
        mid = (start + end) // 2
        left_val = self.seg_tree[node*2]
        if left_val >= nth:
            return self.get_nth_smaller(node*2, start, mid, nth)
        return self.get_nth_smaller(node*2+1, mid+1, end, nth-left_val)

    def get_nth_bigger(self, node, start, end, nth):
        if self.seg_tree[node] < nth: return -1
        if start == end: return start
        mid = (start + end) // 2
        right_val = self.seg_tree[node*2+1]
        if right_val >= nth:
            return self.get_nth_bigger(node*2+1, mid+1, end, nth)
        return self.get_nth_bigger(node*2, start, mid, nth-right_val)