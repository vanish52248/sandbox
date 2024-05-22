package main

import "fmt"

func main() {
	var N, Q int
	fmt.Scan(&N, &Q)

	card_list := []string{}
	for i := 0; i < N; i++ {
		card_list = append(card_list, "N")
	}

	for i := 0; i < Q; i++ {
		var E, Q int
		fmt.Scan(&E, &Q)

		if E == 1 {
			card_list[Q-1] += "Y"
			if card_list[Q-1] == "NYY" {
				card_list[Q-1] = "E"
			}
		} else if E == 2 {
			card_list[Q-1] = "E"
		} else if E == 3 {
			if card_list[Q-1] == "E" {
				fmt.Println("Yes")
			} else {
				fmt.Println("No")
			}
		}
	}
}
