package main

import "fmt"

func main() {
	var a, b, c int
	fmt.Scan(&a, &b, &c)
	pa1 := a + b
	pa2 := a + c
	pa3 := b + c

	lst := [3]int{pa1, pa2, pa3}

	ans := 200001
	for _, v := range lst {
		if v < ans {
			ans = v
		}
	}
	fmt.Println(ans)

}
