package main

import (
	"fmt"
	"strings"
)

func main() {
	var S string
	fmt.Scan(&S)

	isSan := strings.HasSuffix(S, "san")

	if isSan {
		fmt.Println("Yes")
	} else {
		fmt.Println("No")
	}
}
