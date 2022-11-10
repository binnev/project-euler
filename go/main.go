package main

import (
	"euler/puzzles"
	"euler/utils"
)

func main() {
	utils.Assert(
		utils.Profile(puzzles.Euler8),
		"23514624000",
	)
}
