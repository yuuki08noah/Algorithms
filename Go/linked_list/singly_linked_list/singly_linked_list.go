package singly_linked_list

import (
	"errors"
	"fmt"
)

func NewNode[T any](data T, next *Node[T]) *Node[T] {
	return &Node[T]{data: data, next: next}
}

func InitSinglyLinkedList[T any](data T) *Node[T] {
	return NewNode(data, nil)
}

func (node *Node[T]) InsertFirst(data T) *Node[T] {
	return NewNode(data, node)
}

func (node *Node[T]) InsertMiddle(data T, pre *Node[T]) {
	newNode := NewNode(data, pre.next)
	pre.next = newNode
}

func (node *Node[T]) InsertLast(data T) {
	for node.next != nil {
		node = node.next
	}
	node.next = NewNode(data, nil)
}

func (node *Node[T]) DeleteFirst() (*Node[T], error) {
	if node == nil {
		return nil, errors.New("Node is nil")
	}
	newHead := node.next
	return newHead, nil
}

func (node *Node[T]) DeleteMiddle(pre *Node[T]) error {
	if pre.next == nil {
		return errors.New("Node is nil")
	}
	remove := pre.next
	pre.next = remove.next
	return nil
}

func (node *Node[T]) DeleteLast() error {
	if node == nil {
		return errors.New("Node is nil")
	}
	for node.next.next != nil {
		node = node.next
	}
	node.next = nil
	return nil
}

func (node *Node[T]) PrintSinglyLinkedList() {
	for node.next != nil {
		fmt.Print(node.data, " ")
		node = node.next
	}
	fmt.Println(node.data)
}

func (node *Node[T]) Reverse() *Node[T] {
	p := node
	var q *Node[T] = nil
	var r *Node[T] = nil
	for p != nil {
		r = q
		p = p.next
		q.next = r
	}
	return q
}
