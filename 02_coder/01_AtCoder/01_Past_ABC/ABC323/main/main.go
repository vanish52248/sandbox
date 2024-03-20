package main

import (
	"fmt"
)

func main() {
	var S string
	fmt.Scan(&S)

	for i, v := range S {
		if i+1 > 0 && (i+1)%2 == 0 {
			if string(v) != "0" {
				fmt.Println("No")
				return
			}
		}
	}
	fmt.Println("Yes")
}
