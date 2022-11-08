package puzzles

import "fmt"

func Euler2() string {
	const N = 4e6
	a := 1
	b := 2
	c := 0
	total_even := b

	for {
		c = a + b
		a = b
		b = c

		if c <= N && (c%2 == 0) {
			total_even += c
		}
		if c > N {
			break
		}
	}
	return fmt.Sprint(total_even)
}
