package main

import "fmt"

func main() {
	var S string
	fmt.Scan(&S)

	word := ""
	for _, v := range S {
		if string(v) == "a" || string(v) == "e" || string(v) == "i" || string(v) == "o" || string(v) == "u" {
			continue
		}
		word += string(v)
	}

	fmt.Println(word)
}
