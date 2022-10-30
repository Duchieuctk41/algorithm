package main

import (
	"fmt"
)

func twoSum(nums []int, target int) []int {
	seen := map[int]int{}
	for i, value := range nums {
		remaining := target - nums[i]

		if _, ok := seen[remaining]; ok {
			return []int{seen[remaining], i}
		}

		seen[value] = i
	}
	return []int{}
}

func main() {
	nums := []int{-3, 4, 3, 90}
	target := 0
	fmt.Println(twoSum(nums, target))
}
