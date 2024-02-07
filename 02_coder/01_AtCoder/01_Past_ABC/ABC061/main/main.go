package main

import "fmt"

func main() {

	var a, b, c int
	fmt.Scanf("%d %d %d\n", &a, &b, &c)

	if b >= c && c >= a {
		fmt.Println("Yes")
	} else {
		fmt.Println("No")
	}
}
