package main

import (
	"euler/puzzles"
	"euler/utils"
)

func main() {
	utils.Assert(
		utils.Profile(puzzles.Euler10),
		"142913828922",
	)
}
