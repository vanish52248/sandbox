package main

import (
	"fmt"
)

func main() {
	var n int
	fmt.Scan(&n)

	m := make(map[int]bool)

	for i := 1; i <= n; i++ {
		var a int
		fmt.Scan(&a)

		if !m[i] {
			m[a] = true
		}
	}

	var count int
	sl := []int{}

	for i := 1; i <= n; i++ {
		if !m[i] {
			count++
			sl = append(sl, i)
		}
	}

	fmt.Println(count)

	for _, v := range sl {
		fmt.Print(v, " ")
	}
}
