package main

import "fmt"

type Student struct {
	name    string
	math    float64
	english float64
}

func (student Student) CallAvg() {
	fmt.Println(student.name, (student.english+student.math)/2)
}

func main() {
	s1 := Student{"test", 40, 50}
	s1.CallAvg()

}
