package main

import (
	"fmt"
)

func main() {
	var N string
	fmt.Scan(&N)

	start := string(N[0])
	end := string(N[len(N)-1])

	if N == "100" {
		fmt.Println(100)
	} else if len(N) == 1 {
		if start == "0" {
			fmt.Println("0")
		} else if start <= "2" {
			fmt.Println("0")
		} else if start <= "7" {
			fmt.Println("5")
		} else if start >= "8" {
			fmt.Println("10")
		}
	} else if end == "0" {
		fmt.Println(string(N[0]) + "0")
	} else if end == "5" {
		fmt.Println(string(N[0]) + "5")
	} else if end <= "2" {
		fmt.Println(string(N[0]) + "0")
	} else if end <= "4" {
		fmt.Println(string(N[0]) + "5")
	} else if end <= "7" {
		fmt.Println(string(N[0]) + "5")
	} else if end <= "9" {
		if start == "9" {
			fmt.Println(100)
		} else {
			fmt.Println(string(N[0]+1) + "0")
		}
	}
}
