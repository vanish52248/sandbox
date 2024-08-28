package main

import (
	"fmt"
)

func main() {
	var S, T string
	fmt.Scan(&S, &T)

	i := 0
	for _, v := range S {
		for i < len(T) {
			if string(v) == string(T[i]) {
				fmt.Print(i+1, " ")
				i++
				break
			}
			i++
		}
	}

}
