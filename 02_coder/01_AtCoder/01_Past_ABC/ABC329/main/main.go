package main

import "fmt"

func main() {
	var S string
	fmt.Scan(&S)

	current := ""
	for i, v := range S {
		if i == 0 {
			current += string(v)
			continue
		}
		current += " " + string(v)
	}
	fmt.Println(current)
}
