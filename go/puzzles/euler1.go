package puzzles

import (
	"fmt"
)

func Euler1() string {
	const N = 1000
	total := 0
	for ii := 0; ii < N; ii++ {
		if (ii%3 == 0) || (ii%5 == 0) {
			total += ii
		}
	}
	return fmt.Sprint(total)
}
