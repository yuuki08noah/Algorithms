package queue

import (
	"errors"
	"fmt"
)

type Deque[T any] struct {
	data              []T
	rear, front, size int
}

func InitDeque[T any](size int) *Deque[T] {
	deque := new(Deque[T])
	deque.data = make([]T, size)
	deque.front = 0
	deque.rear = 0
	deque.size = size
	return deque
}

func (q *Deque[T]) isEmpty() bool {
	return q.front == q.rear
}

func (q *Deque[T]) isFull() bool {
	return (q.rear+1)%q.size == q.front
}

func (q *Deque[T]) AddFront(value T) error {
	if q.isFull() {
		return errors.New("Deque is full")
	}
	q.data[q.front] = value
	q.front = (q.front - 1 + q.size) % q.size
	return nil
}

func (q *Deque[T]) AddRear(value T) error {
	if q.isFull() {
		return errors.New("Deque is full")
	}
	q.rear = (q.rear + 1) % q.size
	q.data[q.rear] = value
	return nil
}

func (q *Deque[T]) GetFront() (T, error) {
	var value T
	if q.isEmpty() {
		return value, errors.New("Deque is empty")
	}
	q.front = (q.front + 1) % q.size
	q.data[q.front] = value
	return value, nil
}

func (q *Deque[T]) GetRear() (T, error) {
	var value T
	if q.isEmpty() {
		return value, errors.New("Deque is empty")
	}
	value = q.data[q.rear]
	q.rear = (q.rear - 1 + q.size) % q.size
	return value, nil
}

func (q *Deque[T]) PrintDeque() {
	for i := (q.front + 1) % q.size; i != q.rear; i = (i + 1) % q.size {
		fmt.Print(q.data[i], " ")
	}
	fmt.Println(q.data[q.rear])
}
