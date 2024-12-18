package math

import (
	"math/rand"
)

func NewtonsMethod(equation []float64) float64 {
	degree := len(equation) - 1
	derivative := make([]float64, degree)
	for i := degree; i >= 1; i-- {
		derivative[len(equation)-i-1] = equation[len(equation)-i-1] * float64(i)
	}
	var x float64 = rand.Float64()
	for i := 0; i < 1000; i++ {
		x -= Function(equation, x) / Function(derivative, x)
	}
	return x
}
