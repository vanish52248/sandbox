package main

import (
	"fmt"
)

func main() {
	var X, Y int
	fmt.Scan(&X, &Y)

	if X-3 <= Y && Y <= X+2 {
		fmt.Println("Yes")
	} else {
		fmt.Println("No")
	}
}
