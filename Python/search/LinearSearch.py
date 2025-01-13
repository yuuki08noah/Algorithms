class LinearSearch:
    def __init__(self, arr):
        self.arr = arr

    def search(self, key):
        for i in range(len(self.arr)):
            if self.arr[i] == key:
                return i
        return None