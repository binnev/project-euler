package puzzles

import (
	"fmt"
	"math"
)

func PrimeFactors(number int) map[int]int {
	factors := make(map[int]int)
	remainder := number
	product := 1
	p := 2
	limit := int(math.Sqrt(float64(number)))
	for {
		if product == number {
			break
		}
		if p <= limit {
			for {
				if remainder%p != 0 {
					break
				}
				factors[p] += 1
				remainder = remainder / p
				product *= p
			}
			increment := 2
			if p%2 == 0 {
				increment = 1
			}
			p += increment
		} else if remainder != 1 {
			factors[remainder] += 1
			product *= remainder
		}
	}
	return factors
}

func Euler3() string {
	factors := PrimeFactors(600851475143)
	max := 0
	for k, _ := range factors {
		if k > max {
			max = k
		}
	}
	return fmt.Sprint(max)
}
