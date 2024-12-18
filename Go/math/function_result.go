package math

import "math"

func Function(equation []float64, x float64) float64 {
	degree := len(equation) - 1
	var res float64
	for i := degree + 1; i >= 1; i-- {
		res += math.Pow(x, float64(i-1)) * equation[len(equation)-i]
	}
	return res
}
