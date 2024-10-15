class BinarySearch:
    def binary_search_recursive(self, arr, target, start, end):  # 재귀 구현
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid

        if start > end:
            return -1

        if arr[mid] > target:
            return self.binary_search_recursive(arr, target, start, mid - 1)
        else:
            return self.binary_search_recursive(arr, target, mid + 1, end)

    def binary_search_loop(self, arr, target, start, end):  # 반복문 구현
        while start <= end:
            mid = (start + end) // 2
            if arr[mid] == target:
                return mid
            if arr[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return -1
