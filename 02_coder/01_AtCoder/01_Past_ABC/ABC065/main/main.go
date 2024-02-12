package main

import "fmt"

func main() {
	var x, a, b int
	fmt.Scan(&x, &a, &b)
	day := (0 - a) + b

	if day > 0 {
		if day > x {
			fmt.Println("dangerous")
		} else {
			fmt.Println("safe")
		}
	} else {
		fmt.Println("delicious")
	}

}
