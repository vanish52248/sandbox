package main

import "fmt"

func main() {
	var N int
	fmt.Scan(&N)

	list := []int{}
	for i := 0; i < N; i++ {
		var A int
		fmt.Scan(&A)

		list = append(list, A)
	}

	current := 0
	ans := 0
	for i, v := range list {
		if i == 0 {
			current = v
			continue
		}
		ans = current * v
		fmt.Print(ans, " ")
		current = v
	}
}
