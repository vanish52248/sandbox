package main

import "fmt"

func main() {
	count := 0
	for i := 1; i <= 12; i++ {
		var S string
		fmt.Scan(&S)
		if len(S) == i {
			count++
		}
	}
	fmt.Println(count)
}
