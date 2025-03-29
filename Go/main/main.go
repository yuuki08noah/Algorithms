package main

import (
	"algorithms/SNU"
)

func main() {
	var bigDecimal SNU.BigDecimalInterface

	bigDecimal = SNU.BigDecimal{}
	bigDecimal = bigDecimal.Init("9999999999")
	bigDecimal2 := SNU.BigDecimal{}.Init("1")
	bigDecimal.Add(bigDecimal2).Print()
}
