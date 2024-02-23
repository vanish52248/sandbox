package main

import "fmt"

func main() {
	var s1, s2, s3, s4, s5, s6, s7, s8 int
	fmt.Scan(&s1, &s2, &s3, &s4, &s5, &s6, &s7, &s8)
	var list = []int{s1, s2, s3, s4, s5, s6, s7, s8}

	before := 0
	for _, v := range list {

		if before > v {
			fmt.Println("No")
			return
		}

		if !(100 <= v && v <= 675) {
			fmt.Println("No")
			return
		}

		if v%25 != 0 {
			fmt.Println("No")
			return
		}

		before = v
	}
	fmt.Println("Yes")
}
