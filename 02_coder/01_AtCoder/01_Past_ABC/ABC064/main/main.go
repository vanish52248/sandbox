package main

import (
	"fmt"
	"strconv"
)

func main() {
	// var r, g, b int
	var r, g, b string
	fmt.Scan(&r, &g, &b)
	calc, _ := strconv.Atoi(r + g + b)
	// fmt.Println(reflect.TypeOf(calc))

	if calc%4 == 0 {
		fmt.Println("YES")
	} else {
		fmt.Println("NO")
	}

}
