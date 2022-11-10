package main

import (
	"euler/puzzles"
	"euler/utils"
)

func main() {
	utils.Assert(
		utils.Profile(puzzles.Euler6),
		"25164150",
	)
}
