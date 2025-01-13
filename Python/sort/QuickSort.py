class QuickSort:
    def partition(self, arr, left, right):
        pivot = arr[left]
        low = left
        high = right
        while low < high:
            low += 1
            while low <= right and arr[low] <= pivot:
                low += 1
            while arr[high] > pivot:
                high -= 1
            if low < high:
                arr[low], arr[high] = arr[high], arr[low]
        arr[left], arr[high] = arr[high], arr[left]
        return high

    def quicksort(self, arr, start, end):
        if start < end:
            index = self.partition(arr, start, end)
            self.quicksort(arr, start, index - 1)
            self.quicksort(arr, index + 1, end)