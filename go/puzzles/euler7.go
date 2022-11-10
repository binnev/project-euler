package puzzles

import (
	"euler/utils"
	"fmt"
)

func Euler7() string {
	const N = 10000
	primes := utils.SievePrimes(150000)
	return fmt.Sprint(primes[N])
}
