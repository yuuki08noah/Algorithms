package main

import (
	"algorithms"
	"fmt"
)

func main() {
	s := Go.InitStack[int](10)
	s.Push(10)
	s.Push(20)
	s.Push(30)
	s.PrintStack()
	s.Pop()
	s.PrintStack()
	for true {
		value, err := s.Pop()
		if err != nil {
			fmt.Println(err)
			break
		}
		fmt.Println(value)
	}
}
