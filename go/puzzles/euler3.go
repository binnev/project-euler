package puzzles

import (
	"euler/utils"
	"fmt"
)

func Euler3() string {
	factors := utils.PrimeFactors(600851475143)
	max := 0
	for k, _ := range factors {
		if k > max {
			max = k
		}
	}
	return fmt.Sprint(max)
}
