package main

import "fmt"

func main() {
	var N int
	fmt.Scan(&N)

	var count int
	var weekTotal int
	for i := 0; i < 7*N; i++ {
		var a int
		fmt.Scan(&a)

		weekTotal += a

		count++
		if count%7 == 0 {
			fmt.Println(weekTotal)
			weekTotal = 0
		}
	}
}
