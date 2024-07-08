package main

import "fmt"

func main() {

	var N, M int

	fmt.Scan(&N, &M)

	list := []int{}
	for i := 0; i < N; i++ {
		var H int
		fmt.Scan(&H)
		list = append(list, H)

	}
	count := 0

	for _, v := range list {
		if M -= v; M >= 0 {
			count++
		} else {
			fmt.Println(count)
			return
		}
	}
	fmt.Println(count)

}
