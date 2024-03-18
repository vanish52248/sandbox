package main

import (
	"fmt"
	"strings"
)

func main() {
	var N int
	var S string
	fmt.Scan(&N, &S)

	word := ""
	for i := 1; i <= N; i++ {
		word += string(S[i-1])
		if strings.Contains(string(word), "ABC") {
			fmt.Println(i - 2)
			return
		}
	}
	fmt.Println(-1)
}
