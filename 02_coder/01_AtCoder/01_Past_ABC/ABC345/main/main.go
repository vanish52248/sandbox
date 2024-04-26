package main

import (
	"fmt"
	"strings"
)

func main() {
	var S string

	fmt.Scanf("%s", &S)

	var equals = S[1 : len(S)-1]

	fmt.Println(equals)

	if S[0] == '<' && S[len(S)-1] == '>' && strings.Count(equals, "=") == len(S)-2 {
		fmt.Print("Yes")
	} else {
		fmt.Print(("No"))
	}
}
