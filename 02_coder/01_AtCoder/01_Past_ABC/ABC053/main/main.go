package main

import "fmt"

func main() {
	var x int
	fmt.Scanf("%d\n", &x)

	if x < 1200 {
		fmt.Println("ABC")
	} else {
		fmt.Println("ARC")
	}
}
