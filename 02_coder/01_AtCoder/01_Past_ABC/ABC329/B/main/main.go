package main

import (
	"fmt"
	"sort"
)

type IntSlice []int

func (s IntSlice) Len() int           { return len(s) }
func (s IntSlice) Less(i, j int) bool { return s[i] > s[j] }
func (s IntSlice) Swap(i, j int)      { s[i], s[j] = s[j], s[i] }

func maxInt(a []int) int {
	sort.Sort(sort.IntSlice(a))
	return a[len(a)-1]
}

func main() {
	var N int
	fmt.Scan(&N)

	list := []int{}
	for i := 0; i < N; i++ {
		var A int
		fmt.Scan(&A)
		list = append(list, A)
	}

	maxNum := maxInt(list)
	sort.Sort(IntSlice(list))

	for _, v := range list {
		if v != maxNum {
			fmt.Println(v)
			return
		}
	}
}
