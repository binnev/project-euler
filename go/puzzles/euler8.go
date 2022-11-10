package puzzles

import (
	"euler/utils"
	"fmt"
	"strconv"
	"strings"
)

func euler8PythonStyle() string {
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

func euler8GoStyle() string {
	numStr := strings.Join(
		strings.Fields(utils.LoadPuzzleInput("euler8")),
		"",
	)
	length := 13
	maxProd := 0
	for ii := 0; ii < len(numStr)-1-length; ii++ {
		subStr := numStr[ii : ii+length]
		prod := 1
		for _, digitStr := range subStr {
			digit, _ := strconv.Atoi(string(digitStr))
			prod *= digit
		}
		if prod > maxProd {
			maxProd = prod
		}
	}

	return fmt.Sprint(maxProd)
}

func Euler8() string {
	return euler8GoStyle()
}
