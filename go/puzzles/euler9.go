package puzzles

import (
	"euler/utils"
	"fmt"
)

func euler9Brute() string {
	const N = 1000
	for a := 1; a < N; a++ {
		for b := 1; b < N; b++ {
			for c := 1; c < N; c++ {
				if a+b+c == 1000 {
					if utils.IntPow(a, 2)+utils.IntPow(b, 2) == utils.IntPow(c, 2) {
						return fmt.Sprint(a * b * c)
					}
				}
			}
		}
	}
	return ""
}

func euler9Smarter() string {
	const N = 1000
	for a := 1; a < N; a++ {
		for b := 1; b < (N - a); b++ {
			c := N - a - b
			if utils.IntPow(a, 2)+utils.IntPow(b, 2) == utils.IntPow(c, 2) {
				return fmt.Sprint(a * b * c)
			}
		}
	}
	return ""
}

func Euler9() string {
	return euler9Smarter()
}
