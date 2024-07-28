package main

import "fmt"

func main() {
	var N int
	fmt.Scan(&N)

	list := []string{}
	for i := 0; i < N; i++ {
		var S string
		fmt.Scan(&S)
		list = append(list, S)
	}

	count := 0
	for i, v := range list {
		if v == "sweet" {
			count++
			if count == 2 && i != len(list)-1 {
				fmt.Println("No")
				return
			}
		} else {
			count = 0
		}
	}
	fmt.Println("Yes")
}
