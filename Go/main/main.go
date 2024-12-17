package main

import (
	"algorithms/search"
	"algorithms/sort"
	"fmt"
)

func main() {
	arr := []int{8, 1, 7, 2, 9, 2, 3, 1, 3, 7, 6, 0, -1, 2}
	fmt.Println(arr)
	sort.MergeSort(arr)
	fmt.Println(arr)
	fmt.Println(search.BinarySearchRepeated(arr, 6))
}
