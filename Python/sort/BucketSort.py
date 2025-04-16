from Python.sort.QuickSort import QuickSort


class BucketSort:
    def __init__(self, arr):
        self.arr = arr
        self.n = len(arr)
        self.buckets = [[] for _ in range(10000)]

    def sort(self):
        for i in self.arr:
            self.buckets[int(i*10)].append(i)
            if len(self.buckets[int(i * 10)]) > 1:
                QuickSort(self.buckets[int(i*10)])

    def print(self):
        for i in self.buckets:
            if len(i) > 0: print(*i, sep=' ', end=' ')