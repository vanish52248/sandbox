package main

import "fmt"

func main() {
	var AB, AC, BC string
	fmt.Scan(&AB, &AC, &BC)

	//  AB < なら A は B より年下 AB > なら A は B より 年上
	//  AC < なら A は C より年下 AC > なら A は C より 年上
	//  BC < なら B は C より年下 BC > なら B は C より 年上
	if AB != AC {
		fmt.Println("A")
	} else if AB == BC {
		fmt.Println("B")
	} else {
		fmt.Println("C")
	}
}
