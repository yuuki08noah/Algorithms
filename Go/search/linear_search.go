package search

func LinearSearch[T comparable](arr []T, item T) (index int, found bool) {
	for i := 0; i < len(arr); i++ {
		if arr[i] == item {
			return i, true
		}
	}
	return index, false
}
