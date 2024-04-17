package main

import "fmt"

func main() {
	var S string
	fmt.Scan(&S)

	word := ""
	for _, v := range S {
		if string(v) == "." {
			word = ""
		} else {
			word += string(v)
		}
	}
	fmt.Println(word)
}
