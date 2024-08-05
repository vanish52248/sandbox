package main

import "fmt"

func main() {
	var Y int
	fmt.Scan(&Y)

	year := 0
	if Y%4 != 0 {
		year = 365
	}

	if Y%4 == 0 && Y%100 != 0 {
		year = 366
	}

	if Y%100 == 0 && Y%400 != 0 {
		year = 365
	}

	if Y%400 == 0 {
		year = 366
	}

	fmt.Println(year)
}
