package main

import "fmt"

func main() {
	var S string
	fmt.Scan(&S)

	count := 0
	word := ""
	for _, v := range S {
		if string(v) == "|" {
			count++
			continue
		}
		if count == 0 || count >= 2 {
			word += string(v)
		} else if count == 1 {
			continue
		}
	}
	fmt.Println(word)
}
