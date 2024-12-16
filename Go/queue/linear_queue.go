package queue

import (
	"errors"
	"fmt"
)

type LinearQueue[T any] struct {
	data              []T
	rear, front, size int
}

func InitLinearQueue[T any](size int) *LinearQueue[T] {
	queue := new(LinearQueue[T])
	queue.data = make([]T, size)
	queue.front = -1
	queue.rear = -1
	queue.size = size
	return queue
}

func (q *LinearQueue[T]) isEmpty() bool {
	return q.front == q.rear
}

func (q *LinearQueue[T]) isFull() bool {
	return q.rear == q.size-1
}

func (q *LinearQueue[T]) Enqueue(value T) error {
	if q.isFull() {
		return errors.New("Queue is full")
	}
	q.rear++
	q.data[q.rear] = value
	return nil
}

func (q *LinearQueue[T]) Dequeue() (T, error) {
	var value T
	if q.isEmpty() {
		return value, errors.New("Queue is empty")
	}
	q.front++
	q.data[q.front] = value
	return value, nil
}

func (q *LinearQueue[T]) PrintLinearQueue() {
	for i := q.front + 1; i <= q.rear; i++ {
		fmt.Print(q.data[i], " ")
	}
	fmt.Println()
}
