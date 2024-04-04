package main

import "fmt"

func main() {
	var M, D, y, m, d int
	fmt.Scan(&M, &D, &y, &m, &d)

	var year, month, day int
	if (d + 1) > D {
		day = 1
		if (m + 1) > M {
			month = 1
			year = y + 1
		} else {
			month = m + 1
			year = y
		}
	} else {
		day = d + 1
		month = m
		year = y
	}
	fmt.Println(year, month, day)
}
