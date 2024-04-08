package main

import "fmt"

func main() {
	var B, G int
	fmt.Scan(&B, &G)

	if B > G {
		fmt.Println("Bat")
	} else {
		fmt.Println("Glove")
	}
}
