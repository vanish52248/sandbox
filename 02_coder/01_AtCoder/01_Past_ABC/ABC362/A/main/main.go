package main

import (
	"fmt"
	"sort"
)

func main() {
	var R, G, B int
	fmt.Scan(&R, &G, &B)

	var C string
	fmt.Scan(&C)

	list := []int{}
	if C == "Red" {
		list = append(list, G)
		list = append(list, B)
	} else if C == "Green" {
		list = append(list, R)
		list = append(list, B)
	} else if C == "Blue" {
		list = append(list, R)
		list = append(list, G)
	}

	sort.Sort(sort.IntSlice(list))
	fmt.Println(list[0])
}
