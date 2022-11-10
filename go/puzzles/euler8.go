package puzzles

import (
	"euler/utils"
	"fmt"
	"strconv"
	"strings"
)

func Euler8() string {
	numStr := strings.Join(
		strings.Fields(utils.LoadPuzzleInput("euler8")),
		"",
	)
	length := 13
	products := []int{}
	for ii := 0; ii < len(numStr)-1-length; ii++ {
		subStr := numStr[ii : ii+length]
		digits := []int{}
		for _, digitStr := range subStr {
			digit, _ := strconv.Atoi(string(digitStr))
			digits = append(digits, digit)
		}
		products = append(products,
			utils.ProductInt(digits),
		)
	}

	return fmt.Sprint(utils.MaxInt(products))
}
