package main

import "fmt"

func main() {
	var a, b string
	fmt.Scanf("%s %s\n", &a, &b)

	if a == "H" {
		fmt.Println(b)
	} else if a == "D" {
		if b == "H" {
			fmt.Println("D")
		} else if b == "D" {
			fmt.Println("H")
		}
	}

}
