package main

import "fmt"

func main() {

	var N int
	fmt.Scanf("%d\n", &N)

	x := N * 800
	y := (N / 15) * 200

	fmt.Println(x - y)
}
