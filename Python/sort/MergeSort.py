class MergeSort:
    def __init__(self, arr):
        self.arr = arr
        self.length = len(arr)
        self.sort(0, self.length - 1)

    def sort(self, left, right):
        if left < right:
            mid = (left + right) // 2
            self.sort(left, mid)
            self.sort(mid + 1, right)
            self.merge(left, right)

    def merge(self, left, right):
        mid = (left + right) // 2
        low, high, index = left, mid + 1, 0
        sorted_arr = [0] * (right - left + 1)
        while low <= mid and high <= right:
            if self.arr[low] < self.arr[high]:
                sorted_arr[index] = self.arr[low]
                low += 1
            else:
                sorted_arr[index] = self.arr[high]
                high += 1
            index += 1

        for i in range(low, mid + 1):
            sorted_arr[index] = self.arr[i]
            index += 1

        for i in range(high, right + 1):
            sorted_arr[index] = self.arr[i]
            index += 1

        for i in range(left, right + 1):
            self.arr[i] = sorted_arr[i - left]
