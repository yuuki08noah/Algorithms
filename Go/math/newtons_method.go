package math

import (
	"math"
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
		x -= function(equation, x) / function(derivative, x)
	}
	return x
}

func function(equation []float64, x float64) float64 {
	degree := len(equation) - 1
	var res float64
	for i := degree + 1; i >= 1; i-- {
		res += math.Pow(x, float64(i-1)) * equation[len(equation)-i]
	}
	return res
}
