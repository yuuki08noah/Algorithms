package main

import "algorithms/linked_list"

func main() {
	head := linked_list.InitSinglyLinkedList[int](10)
	head.InsertLast(30)
	head.InsertLast(40)
	head = head.InsertFirst(50)
	head.InsertMiddle(999, head)
	head.PrintSinglyLinkedList()
	head.DeleteLast()
	head.DeleteFirst()
	head.PrintSinglyLinkedList()
	head.DeleteMiddle(head)
	head.DeleteLast()
	head.PrintSinglyLinkedList()
}
