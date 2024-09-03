package collection

import "sort"

func maxInt(a []int) int {
	sort.Sort(sort.IntSlice(a))
	return a[len(a)-1]
}

func minInt(a []int) int {
	sort.Sort(sort.IntSlice(a))
	return a[0]
}
