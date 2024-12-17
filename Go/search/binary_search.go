package search

import (
	"golang.org/x/exp/constraints"
)

func BinarySearchRecursive[T constraints.Ordered](arr []T, left int, right int, value T) (index int, found bool) {
	if left <= right {
		mid := (left + right) / 2
		if arr[mid] == value {
			return mid, true
		} else if arr[mid] < value {
			return BinarySearchRecursive[T](arr, mid+1, right, value)
		} else {
			return BinarySearchRecursive[T](arr, left, mid-1, value)
		}
	}
	return index, found
}

func BinarySearchRepeated[T constraints.Ordered](arr []T, value T) (index int, found bool) {
	left, right := 0, len(arr)-1
	for left <= right {
		mid := (left + right) / 2
		if arr[mid] == value {
			return mid, true
		} else if arr[mid] < value {
			left = mid + 1
		} else {
			right = mid - 1
		}
	}
	return index, found
}
