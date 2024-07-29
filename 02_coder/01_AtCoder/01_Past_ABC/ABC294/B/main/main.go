package main

import "fmt"

func main() {
	var H, W int
	fmt.Scan(&H, &W)

	var list = [26]string{"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"}

	for i := 0; i < H; i++ {
		for j := 0; j < W; j++ {
			var A int
			fmt.Scan(&A)
			if A == 0 {
				fmt.Print(".")
			} else {
				fmt.Print(list[A-1])
			}
		}
		fmt.Println()
	}

}
