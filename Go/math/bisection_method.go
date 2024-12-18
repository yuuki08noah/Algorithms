package math

func BisectionMethod(equation []float64) float64 {
	start, end := float64(-1000000000), float64(1000000000)
	var mid float64
	for i := 0; i < 1000; i++ {
		mid = (start + end) / 2
		res := Function(equation, mid)
		if res < 0 {
			start = mid
		} else if res > 0 {
			end = mid
		} else {
			return mid
		}
	}
	return mid
}
