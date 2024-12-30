package tree

import (
	"fmt"
	"golang.org/x/exp/constraints"
)

type Node[T constraints.Ordered] struct {
	data        T
	left, right *Node[T]
	parent      *Node[T]
	level       int
	direction   bool
}

type BinarySearchTree[T constraints.Ordered] struct {
	root *Node[T]
}

func NewNode[T constraints.Ordered](value T, left *Node[T], right *Node[T], parent *Node[T], level int, direction bool) *Node[T] {
	return &Node[T]{data: value, left: left, right: right, parent: parent, level: level, direction: direction}
}

func InitBinarySearchTree[T constraints.Ordered]() *BinarySearchTree[T] {
	return &BinarySearchTree[T]{nil}
}

func (bst *BinarySearchTree[T]) Insert(value T) {
	now := bst.root
	if bst.root == nil {
		bst.root = NewNode(value, nil, nil, nil, 1, false)
	} else {
		temp := now
		level := 1
		for now != nil {
			temp = now
			if now.data < value {
				now = now.right
			} else {
				now = now.left
			}
			level++
		}
		if temp.data < value {
			temp.right = NewNode(value, nil, nil, temp, level, true)
		} else {
			temp.left = NewNode(value, nil, nil, temp, level, false)
		}
	}
}

func (bst *BinarySearchTree[T]) Search(key T) (result bool, node *Node[T]) {
	now := bst.root
	for now != nil {
		if now.data < key {
			now = now.right
		} else if now.data > key {
			now = now.left
		} else {
			return true, now
		}
	}
	return false, now
}

func (bst *BinarySearchTree[T]) Delete(key T) bool {
	res, node := bst.Search(key)
	if !res {
		return false
	}
	if node.left == nil && node.right == nil {
		if node.parent == nil {
			bst.root = nil
		} else if node.direction {
			node.parent.right = nil
		} else {
			node.parent.left = nil
		}
	} else if node.left != nil && node.right != nil {
		temp := node.right
		for temp.left != nil {
			temp = temp.left
		}
		node.data = temp.data
		if temp.direction {
			temp.parent.right = nil
		} else {
			temp.parent.left = nil
		}
	} else {
		now := node.left
		if node.right != nil {
			now = node.right
		}
		if node.parent == nil {
			bst.root = now
		} else if node.direction {
			node.parent.right = now
		} else {
			node.parent.left = now
		}
	}
	return true
}

func (bst *BinarySearchTree[T]) PrintTree(node *Node[T], direction string) {
	fmt.Println(node.level, node.data, direction)
	if node.left != nil {
		bst.PrintTree(node.left, "left")
	}
	if node.right != nil {
		bst.PrintTree(node.right, "right")
	}
}

func (bst *BinarySearchTree[T]) Root() *Node[T] {
	return bst.root
}
