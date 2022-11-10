package puzzles

import (
	"euler/utils"
	"fmt"
)

func Euler6() string {
	const N = 100
	natural := utils.MakeRange(1, N+1)
	sumOfSq := 0
	sumNatural := 0
	for _, n := range natural {
		sumOfSq += utils.IntPow(n, 2)
		sumNatural += n
	}
	sqOfSums := utils.IntPow(sumNatural, 2)
	return fmt.Sprint(sqOfSums - sumOfSq)
}
