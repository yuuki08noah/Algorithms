class QuickSort:
    def __init__(self, arr):
        self.arr = arr
        self.length = len(arr)
        self.quicksort(0, self.length - 1)

    def partition(self, left, right):
        pivot = self.arr[left]
        low = left
        high = right
        while low < high:
            low += 1
            while low <= right and self.arr[low] <= pivot:
                low += 1
            while self.arr[high] > pivot:
                high -= 1
            if low < high:
                self.arr[low], self.arr[high] = self.arr[high], self.arr[low]
        self.arr[left], self.arr[high] = self.arr[high], self.arr[left]
        return high

    def quicksort(self, start, end):
        if start < end:
            index = self.partition(start, end)
            self.quicksort(start, index - 1)
            self.quicksort(index + 1, end)