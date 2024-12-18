package main

import (
	"algorithms/math"
	"fmt"
)

func main() {
	equation := []float64{4, 3, 2, 1}
	fmt.Println(math.NewtonsMethod(equation))
}
