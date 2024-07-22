package main

import "fmt"

func main() {
	var R int
	fmt.Scan(&R)

	if 1 <= R && R <= 99 {
		fmt.Println(100 - R)
	} else if 100 <= R && R <= 199 {
		fmt.Println(200 - R)
	} else if 200 <= R && R <= 299 {
		fmt.Println(300 - R)
	}
}
