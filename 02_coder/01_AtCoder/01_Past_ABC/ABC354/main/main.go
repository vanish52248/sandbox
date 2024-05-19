package main

import (
	"fmt"
)

func main() {
	var H int
	fmt.Scan(&H)

	i := 1
	calc := 2
	count := 1
	for {
		count++
		i += calc
		if H < i {
			fmt.Println(count)
			return
		}
		calc *= 2
	}
}
