package puzzles

import (
	"euler/utils"
	"fmt"
)

func Euler10() string {
	const N = 2000000
	result := utils.Sum(utils.SievePrimes(N))
	return fmt.Sprint(result)
}
