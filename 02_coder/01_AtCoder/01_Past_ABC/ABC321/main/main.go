package main

import (
	"fmt"
)

func main() {
	var N string
	fmt.Scan(&N)

	currentNum := string(N[0])
	for i, v := range N {
		if i == 0 {
			continue
		}

		if currentNum <= string(v) {
			fmt.Println("No")
			return
		}

		currentNum = string(v)
	}
	fmt.Println("Yes")
}
