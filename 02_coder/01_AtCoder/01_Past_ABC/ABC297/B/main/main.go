package main

import "fmt"

func main() {
	var S string
	fmt.Scan(&S)

	bIndexStart := 0
	bIndexEnd := 0
	isAppearedR := false
	appearCount := 0

	for i := 0; i < len(S); i++ {

		currentWord := string(S[i])

		// Rが出現したらカウントアップ
		if currentWord == "R" {
			appearCount++
		}

		// Bの偶奇判定
		if currentWord == "B" && bIndexStart == 0 {
			bIndexStart = i + 1
		} else if currentWord == "B" && bIndexEnd == 0 {
			bIndexEnd = i + 1
		}

		// Kが2つのRの間にあるか判定
		if currentWord == "K" && appearCount == 1 {
			isAppearedR = true
		}

		if currentWord == "K" && appearCount == 2 && !isAppearedR {
			fmt.Println("No")
			return
		}
	}

	if bIndexStart%2 == 0 && bIndexEnd%2 == 0 || !isAppearedR {
		fmt.Println("No")
	} else if bIndexStart%2 != 0 && bIndexEnd%2 != 0 || !isAppearedR {
		fmt.Println("No")
	} else {
		fmt.Println("Yes")
	}
}
