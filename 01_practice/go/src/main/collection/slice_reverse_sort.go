package collection

import (
	"fmt"
	"sort"
)

type IntSlice []int

func (s IntSlice) Len() int           { return len(s) }
func (s IntSlice) Less(i, j int) bool { return s[i] > s[j] }
func (s IntSlice) Swap(i, j int)      { s[i], s[j] = s[j], s[i] }

func reverse() {
	list := []int{5, 2, 9, 1, 5, 6}

	// 降順ソート
	sort.Sort(IntSlice(list))

	fmt.Println(list)
}
