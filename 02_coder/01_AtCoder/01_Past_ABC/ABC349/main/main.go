package main

import (
	"fmt"
	"math"
)

func main() {
	var N int
	fmt.Scan(&N)

	list := []int{}
	for i := 0; i < N-1; i++ {
		var A int
		fmt.Scan(&A)

		list = append(list, A)
	}

	total := 0
	for _, v := range list {
		total += v
	}

	if total < 0 {
		fmt.Println(math.Abs(float64(total)))
	} else if total == 0 {
		fmt.Println(0)
	} else {
		fmt.Println(fmt.Sprintf("-%d", total))
	}

}
