package circular_linked_list

import "errors"

func InitCircularLinkedList[T any](data T) *Node[T] {
	node := &Node[T]{data: data}
	node.next = node
	return node
}

func NewNode[T any](data T, next *Node[T]) *Node[T] {
	return &Node[T]{data: data, next: next}
}

func (node *Node[T]) InsertFirst(data T) *Node[T] {
	newNode := NewNode(data, node.next)
	node.next = newNode
	return newNode
}

func (node *Node[T]) InsertLast(data T) *Node[T] {
	newNode := NewNode(data, node.next)
	node.next = newNode
	node = newNode
	return node
}

func (node *Node[T]) DeleteFirst() (*Node[T], error) {
	if node == nil {
		return nil, errors.New("Node is nil")
	}
	node.next = node.next.next
	return node, nil
}

func (node *Node[T]) DeleteMiddle(pre *Node[T]) error {
	if pre.next == nil {
		return errors.New("Node is nil")
	}
	remove := pre.next
	pre.next = remove.next
	return nil
}
