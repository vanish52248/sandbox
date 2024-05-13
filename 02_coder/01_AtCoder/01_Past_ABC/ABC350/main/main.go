package main

import (
	"fmt"
	"strconv"
)

func main() {
	var S string
	fmt.Scan(&S)

	S2, _ := strconv.Atoi(S[3:])

	if S2 < 001 || S2 == 316 || S2 > 349 {
		fmt.Println("No")
	} else {
		fmt.Println("Yes")
	}

}
