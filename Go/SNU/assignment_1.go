package SNU

import (
	"fmt"
	"strconv"
	"strings"
)

type BigDecimalInterface interface {
	Init(string) BigDecimal
	Add(BigDecimal) BigDecimal
	Sub(BigDecimal) BigDecimal
	Mul(BigDecimal) BigDecimal
	Div(BigDecimal) BigDecimal
	Mod(BigDecimal) BigDecimal
	Print()
}

type BigDecimal struct {
	arr  []int
	size int
}

var MOD = 1000000000

func reverseString(s string) string {
	var builder strings.Builder
	runes := []rune(s)

	for i := len(runes) - 1; i >= 0; i-- {
		builder.WriteRune(runes[i])
	}

	return builder.String()
}

func (a BigDecimal) Init(num string) BigDecimal {
	a.arr = make([]int, len(num)/9+2)
	a.size = len(num)/9 + 1
	num = reverseString(num)

	for i := 0; i < a.size; i++ {
		a.arr[a.size-i], _ = strconv.Atoi(reverseString(num[i*9 : min(i*9+9, len(num))]))
	}

	return a
}

func (b BigDecimal) Print() {
	var result string
	var index int

	for i := 0; i < b.size+1; i++ {
		result = result + fmt.Sprintf("%09d", b.arr[i])
	}

	for i := 0; i < len(result); i++ {
		if result[i] != '0' {
			index = i
			break
		}
	}
	fmt.Println(result[index:])
}

func (a BigDecimal) Add(b BigDecimal) BigDecimal {
	var result string
	var carry int
	for i := 0; i < min(a.size, b.size); i++ {
		temp := a.arr[a.size-i] + b.arr[b.size-i] + carry
		carry = temp / MOD
		result = fmt.Sprintf("%09d", temp%MOD) + result
	}
	if a.size > b.size {
		for i := b.size; i < a.size; i++ {
			temp := a.arr[a.size-i] + carry
			carry = temp / MOD
			result = strconv.Itoa(temp%MOD) + result
		}
	} else {
		for i := a.size; i < b.size; i++ {
			temp := b.arr[b.size-i] + carry
			carry = temp / MOD
			result = strconv.Itoa(temp%MOD) + result
		}
	}
	return BigDecimal{}.Init(result)
}

func (a BigDecimal) Sub(decimal BigDecimal) BigDecimal {
	//TODO ement me
	panic("ement me")
}

func (a BigDecimal) Mul(decimal BigDecimal) BigDecimal {
	//TODO ement me
	panic("ement me")
}

func (a BigDecimal) Div(decimal BigDecimal) BigDecimal {
	//TODO ement me
	panic("ement me")
}

func (a BigDecimal) Mod(decimal BigDecimal) BigDecimal {
	//TODO ement me
	panic("ement me")
}
