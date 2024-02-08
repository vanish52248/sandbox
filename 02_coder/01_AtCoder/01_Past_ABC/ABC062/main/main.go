package main

import (
	"fmt"
)

func main() {
	var x, y int
	fmt.Scan(&x, &y)
	if judge_gr1(x, y) {
		fmt.Println("Yes")
		return
	}

	if judge_gr2(x, y) {
		fmt.Println("Yes")
		return
	}

	if x == 2 && y == 2 {
		fmt.Println("Yes")
		return
	}

	fmt.Println("No")
}

func judge_gr1(x int, y int) bool {
	gr1 := [7]int{1, 3, 5, 7, 8, 10, 12}
	flg_x := false
	flg_y := false

	for _, s := range gr1 {
		if x == s {
			flg_x = true
		}

		if y == s {
			flg_y = true
		}
	}

	if flg_x && flg_y {
		return true
	} else {
		return false
	}
}

func judge_gr2(x int, y int) bool {
	gr1 := [4]int{4, 6, 9, 11}
	flg_x := false
	flg_y := false

	for _, s := range gr1 {
		if x == s {
			flg_x = true
		}

		if y == s {
			flg_y = true
		}
	}

	if flg_x && flg_y {
		return true
	} else {
		return false
	}
}
