package main

import "fmt"

func main() {
	var N, X, Y, Z int

	fmt.Scan(&N, &X, &Y, &Z)
	if X > Y {
		for i := X; i >= Y; i-- {
			if i == Z {
				fmt.Println("Yes")
				return
			}
		}
	} else if X < Y {
		for i := X; i <= Y; i++ {
			if i == Z {
				fmt.Println("Yes")
				return
			}
		}
	}
	fmt.Println("No")

}
