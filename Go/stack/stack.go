package stack

import (
	"errors"
	"fmt"
)

type Stack[T any] struct {
	data []T
	top  int
	size int
}

// 스택 초기화
func InitStack[T any](size int) *Stack[T] {
	stack := new(Stack[T])
	stack.top = -1
	stack.data = make([]T, size)
	stack.size = size
	return stack
}

// 공백 상태 검출
func (s *Stack[T]) isEmpty() bool {
	return s.top == -1
}

// 포화 상태 검출
func (s *Stack[T]) isFull() bool {
	return s.top+1 == s.size
}

// 삽입
func (s *Stack[T]) Push(value T) error {
	if s.isFull() {
		return errors.New("Stack is full")
	}
	s.top++
	s.data[s.top] = value
	return nil
}

// 삭제
func (s *Stack[T]) Pop() (T, error) {
	var value T
	if s.isEmpty() {
		return value, errors.New("Stack is empty")
	}
	value = s.data[s.top]
	s.top--
	return value, nil
}

// 피크
func (s *Stack[T]) Peek() (T, error) {
	var value T
	if s.isEmpty() {
		return value, errors.New("Stack is empty")
	}
	value = s.data[s.top]
	return value, nil
}

func (s *Stack[T]) PrintStack() {
	for i := 0; i <= s.top; i++ {
		fmt.Print(s.data[i], " ")
	}
	fmt.Println()
}
