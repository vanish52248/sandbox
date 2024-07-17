package main

import "fmt"

func main() {
	var S string
	fmt.Scan(&S)

	if string(S[0]) == "R" || (string(S[1]) == "R" && string(S[2]) == "M") {
		fmt.Println("Yes")
	} else {
		fmt.Println("No")
	}
}
