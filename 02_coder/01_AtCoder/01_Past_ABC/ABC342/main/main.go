package main

import (
	"fmt"
	"strings"
)

func main() {
	var S string
	fmt.Scan(&S)

	count1 := 0
	count2 := 0
	word1 := ""
	word2 := ""
	for i, v := range S {
		if i == 0 {
			word1 = string(v)
			count1++
		} else {
			if word1 == string(v) {
				count1++
			} else {
				word2 = string(v)
				count2++
			}
		}
	}
	if count1 > count2 {
		fmt.Println(strings.Index(string(S), word2) + 1)
	} else if count1 < count2 {
		fmt.Println(strings.Index(string(S), word1) + 1)
	}
}
