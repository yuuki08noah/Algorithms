package sort

func SelectionSort(arr []int) {
	for i := 0; i < len(arr); i++ {
		index := i
		for j := i; j < len(arr); j++ {
			if arr[j] < arr[index] {
				index = j
			}
		}
		arr[index], arr[i] = arr[i], arr[index]
	}
}
