package main

import "fmt"

func main() {
	var wordList = []string{"ACE", "BDF", "CEG", "DFA", "EGB", "FAC", "GBD"}

	var S string
	fmt.Scan(&S)

	for _, word := range wordList {
		if S == word {
			fmt.Println("Yes")
			return
		}
	}
	fmt.Println("No")
}
