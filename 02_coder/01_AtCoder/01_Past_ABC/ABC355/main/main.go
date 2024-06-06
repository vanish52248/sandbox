package main

import "fmt"

func main() {
	var A, B int
	fmt.Scan(&A, &B)
	numList := []int{}

	numList = append(numList, A)
	numList = append(numList, B)
	fmt.Println(numList)
}
