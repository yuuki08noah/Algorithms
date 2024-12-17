package main

import (
	"algorithms/sort"
	"fmt"
)

func main() {
	arr := []int{8, 1, 7, 2}
	fmt.Println(arr)
	sort.MergeSort(arr)
	fmt.Println(arr)
}
