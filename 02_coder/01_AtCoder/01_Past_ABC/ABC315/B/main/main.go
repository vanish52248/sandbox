package main

import "fmt"

func main() {
	var M int
	fmt.Scan(&M)

	allDay := []int{}
	halfDay := 0
	for i := 0; i < M; i++ {
		var D int
		fmt.Scan(&D)

		allDay = append(allDay, D)
		halfDay += D
	}

	halfDay = (halfDay + 1) / 2

	month := 1
	day := 1
	currentDay := 0
	for i := 0; i < len(allDay); i++ {
		if currentDay+allDay[i] < halfDay {
			currentDay += allDay[i]
			month++
		} else {
			day = halfDay - currentDay
			break
		}
	}
	fmt.Println(month, day)
}
