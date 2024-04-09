package main

import (
	"fmt"
)

func main() {
	var S string
	fmt.Scan(&S)

	fmt.Println(string(S[:len(S)-1]) + "4")
}
