package puzzles

import (
	"euler/utils"
	"fmt"
	"math"
)

func Euler5() string {
	start, end := 2, 20
	factors := map[int]int{}

	for n := start; n < end; n++ {
		factors_n := utils.PrimeFactors(n)

		for f, p := range factors_n {
			val, ok := factors[f]
			if ok {
				if val < p {
					factors[f] = p
				}
			} else {
				factors[f] = p
			}

		}
	}
	output := 1
	for f, p := range factors {
		output *= int(math.Pow(float64(f), float64(p)))
	}
	return fmt.Sprint(output)
}
