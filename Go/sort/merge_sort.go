package sort

func MergeSort(arr []int) {
	Divide(arr, 0, len(arr)-1)
}

func Divide(arr []int, left int, right int) {
	if left < right {
		mid := (left + right) / 2
		Divide(arr, left, mid)
		Divide(arr, mid+1, right)
		Conquer(arr, left, right)
	}
}

func Conquer(arr []int, left int, right int) {
	sorted := make([]int, right-left+1)
	low := left
	mid := (left + right) / 2
	high := mid + 1
	index := 0

	for low <= mid && high <= right {
		if arr[low] < arr[high] {
			sorted[index] = arr[low]
			index++
			low++
		} else {
			sorted[index] = arr[high]
			index++
			high++
		}
	}
	for low <= mid {
		sorted[index] = arr[low]
		index++
		low++
	}
	for high <= right {
		sorted[index] = arr[high]
		index++
		high++
	}
	for i := left; i <= right; i++ {
		arr[i] = sorted[i-left]
	}
}
