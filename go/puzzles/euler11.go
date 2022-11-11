package puzzles

import (
	"euler/utils"
	"fmt"
	"strconv"
	"strings"
)

func parseGrid() [20][20]int {
	raw := utils.LoadPuzzleInput("euler11")
	rows := strings.Split(raw, "\n")
	const N = 20
	grid := [N][N]int{}
	for y, row := range rows {
		if len(row) == 0 {
			continue
		}
		rowStrings := strings.Fields(row)
		for x, numStr := range rowStrings {
			num, err := strconv.Atoi(string(numStr))
			if err != nil {
				panic(len(row))
			}
			grid[y][x] = num
		}
	}
	return grid
}

func euler11Brute() string {
	const N = 20
	grid := parseGrid()
	span := 4
	maxProd := 0
	for y := 0; y < N-span; y++ {
		for x := 0; x < N-span; x++ {
			hor := [4]int{}
			ver := [4]int{}
			diag := [4]int{}
			diagUp := [4]int{}
			for ii := 0; ii < 4; ii++ {
				hor[ii] = grid[y][x+ii]         // horizontal
				ver[ii] = grid[y+ii][x]         // vertical
				diag[ii] = grid[y+ii][x+ii]     // diagonal down
				diagUp[ii] = grid[y+4-ii][x+ii] // diagonal up
			}
			vectors := [][4]int{hor, ver, diag, diagUp}
			for _, vector := range vectors {
				prod := vector[0] * vector[1] * vector[2] * vector[3]
				if prod > maxProd {
					maxProd = prod
				}
			}
		}
	}
	return fmt.Sprint(maxProd)
}

func Euler11() string {
	return euler11Brute()
}
