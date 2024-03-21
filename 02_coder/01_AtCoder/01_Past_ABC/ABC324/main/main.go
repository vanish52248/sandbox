package main

import "fmt"

func main() {

	var N int
	fmt.Scan(&N)

	var currentList []int
	for i := 0; i < N; i++ {
		var A int
		fmt.Scan(&A)
		currentList = append(currentList, A)
	}

	currentNum := currentList[0]
	for _, v := range currentList {
		if v != currentNum {
			fmt.Println("No")
			return
		}
	}
	fmt.Println("Yes")
}
