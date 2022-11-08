package puzzles

import (
	"euler/utils"
	"fmt"
)

func isPalindromeNumber(number int) bool {
	s := fmt.Sprint(number)
	reversed := utils.ReverseString(s)
	return (s == reversed)
}

func euler4Brute() string {
	palindromes := []int{}

	for ii := 999; ii > 100; ii-- {
		for jj := 999; jj > 100; jj-- {
			number := ii * jj
			if isPalindromeNumber(number) {
				palindromes = append(palindromes, number)
			}
		}
	}

	max := 0
	for _, p := range palindromes {
		if p > max {
			max = p
		}
	}
	return fmt.Sprint(max)
}

func euler4Elegant() string {
	// restrict the "sideways" search space (away from the diagonal) because the
	// palindromes there will be smaller
	const N = 999
	palindromes := []int{}

	candidates := [N - 100]int{}
	for ii, n := 0, N; n > 100; ii, n = ii+1, n-1 {
		candidates[ii] = n
	}
	jj_crit := len(candidates)

	for ii, c := range candidates {
		row := candidates[ii:jj_crit]
		products := []int{}
		for _, r := range row {
			products = append(products, c*r)
		}

		for jj, p := range products {
			if isPalindromeNumber(p) {
				palindromes = append(palindromes, p)
				jj_crit = jj + ii
				break
			}
		}

		if ii >= jj_crit {
			break
		}
	}
	max := 0
	for _, p := range palindromes {
		if p > max {
			max = p
		}
	}
	fmt.Println(palindromes)
	return fmt.Sprint(max)
}

func Euler4() string {
	return euler4Elegant()
}
