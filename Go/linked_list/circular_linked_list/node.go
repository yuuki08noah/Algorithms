package circular_linked_list

type Node[T any] struct {
	data T
	next *Node[T]
}
