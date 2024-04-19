package main

import "fmt"

func main() {
	var N int
	fmt.Scan(&N)

	num := "1"
	for i := 0; i < N; i++ {
		num += "01"
	}
	fmt.Println(num)
}
