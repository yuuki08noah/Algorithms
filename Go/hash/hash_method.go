package hash

import (
	"algorithms/linked_list/singly_linked_list"
)

func LinearProbing[T comparable](arr []T, key int, value T) {
	var emptyValue T
	for arr[key] != emptyValue {
		key += 1
		key %= len(arr)
	}
	arr[key] = value
}

func QuadraticProbing[T comparable](arr []T, key int) {
	var emptyValue T
	i := 1
	for arr[key] != emptyValue {
		key += i * i
		key %= len(arr)
	}
}

func DoubleHashing[T comparable](arr []T, key int) int {
	var emptyValue T
	k := key
	for arr[k] != emptyValue {
		k += IntHash2(key, len(arr))
		k %= len(arr)
	}
	return k
}

func Chaining[T any](arr []*singly_linked_list.Node[T], key int, value T) {
	arr[key].InsertLast(value)
}
