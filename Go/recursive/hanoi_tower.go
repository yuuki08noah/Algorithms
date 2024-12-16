package recursive

import "fmt"

func HanoiTower[T any](n int, from T, tmp T, to T) {
	if n == 1 {
		fmt.Printf("%+v -> %+v\n", from, to)
	} else {
		HanoiTower[T](n-1, from, to, tmp)
		fmt.Printf("%+v -> %+v\n", from, to)
		HanoiTower[T](n-1, tmp, from, to)
	}
}
