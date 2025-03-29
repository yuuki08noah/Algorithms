package tree

import "golang.org/x/exp/constraints"

type Tree[T constraints.Ordered] interface {
	Insert(value T)
	Search(value T) (result bool, node *Node[T])
	Delete(value T) bool
	PrintTree(node *Node[T], direction string)
	Root() *Node[T]
}
