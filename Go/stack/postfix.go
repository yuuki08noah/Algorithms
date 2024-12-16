package stack

func Postfix(expression string) int {
	stack := InitStack[int](len(expression))
	for i := 0; i < len(expression); i++ {
		if expression[i] == ' ' {
			continue
		}
		if int(expression[i]) <= '9' && int(expression[i]) >= '0' {
			var temp int
			for expression[i] != ' ' {
				temp = temp*10 + int(expression[i]) - '0'
				i++
			}
			stack.Push(temp)
		} else {
			val1, _ := stack.Pop()
			val2, _ := stack.Pop()
			switch expression[i] {
			case '+':
				stack.Push(val1 + val2)
			case '-':
				stack.Push(val2 - val1)
			case '*':
				stack.Push(val1 * val2)
			case '/':
				stack.Push(val2 / val1)
			}
		}
	}
	res, _ := stack.Pop()
	return res
}
