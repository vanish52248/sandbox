package main

import "fmt"

func main() {

	var N int
	var S string

	fmt.Scan(&N)
	fmt.Scan(&S)

	A_flg := false
	B_flg := false
	C_flg := false

	for i := 0; i < N; i++ {
		if string(S[i]) == "A" {
			A_flg = true
		} else if string(S[i]) == "B" {
			B_flg = true
		} else if string(S[i]) == "C" {
			C_flg = true
		}

		if A_flg && B_flg && C_flg {
			fmt.Println(i + 1)
			break
		}
	}

}
