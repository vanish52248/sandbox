package main

import (
	"fmt"
	"unicode"
)

func main() {
	var S string
	fmt.Scan(&S)

	for i, v := range S {
		if i == 0 {
			if !unicode.IsUpper(v) {
				fmt.Println("No")
				return
			}
		} else {
			if !unicode.IsLower(v) {
				fmt.Println("No")
				return
			}
		}
	}
	fmt.Println("Yes")
}
