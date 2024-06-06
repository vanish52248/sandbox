package main

import (
	"fmt"
)

func main() {
	var a, b int
	fmt.Scanf("%d", &a)
	fmt.Scanf("%d", &b)

	candidates := []int{1, 2, 3}
	found := -1

	for _, candidate := range candidates {
		if candidate != a && candidate != b {
			if found == -1 {
				found = candidate
			} else {
				found = -1
				break
			}
		}
	}

	fmt.Println(found)

}
