package main

import (
	"algorithms/tree"
)

func main() {
	var bst tree.Tree[int] = tree.InitBinarySearchTree[int]()
	bst.Insert(30)
	bst.Insert(40)
	bst.Insert(50)
	bst.Insert(45)
	bst.Insert(60)
	bst.Insert(20)
	bst.Insert(15)
	bst.Insert(35)
	bst.Delete(30)
	bst.PrintTree(bst.Root(), "root")
}
