package doubly_linked_list

func newNode[T any](data T, next *Node[T], prev *Node[T]) *Node[T] {
	return &Node[T]{data, next, prev}
}

func InitDoublyLinkedList[T any](data T) *Node[T] {
	node := newNode[T](data, nil, nil)
	return node
}

func (node *Node[T]) DeleteMiddle(remove *Node[T]) {
	remove.next.prev = remove.prev
	remove.prev.next = remove.next
	remove = nil
}

func (node *Node[T]) InsertMiddle(before *Node[T], new *Node[T]) {
	new.next = before.next
	new.prev = before
	before.next = new
	new.next.prev = new
}
