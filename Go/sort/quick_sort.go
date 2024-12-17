package sort

func QuickSort(arr []int) {
	Partition(arr, 0, len(arr)-1)
}

func Partition(arr []int, left int, right int) {
	if left < right {
		peek := Sort(arr, left, right)
		Partition(arr, left, peek-1)
		Partition(arr, peek+1, right)
	}
}

func Sort(arr []int, left int, right int) int {
	pivot := arr[left]
	low := left + 1
	high := right

	for {
		for low <= high && arr[low] <= pivot {
			low++
		}
		for low <= high && arr[high] >= pivot {
			high--
		}
		if low > high {
			break
		}
		arr[low], arr[high] = arr[high], arr[low]
	}

	arr[left], arr[high] = arr[high], arr[left]
	return high
}
