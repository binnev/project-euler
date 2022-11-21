package main

import (
	"euler/puzzles"
	"euler/utils"
	"testing"
)

func TestAll(t *testing.T) {
	cases := []struct {
		f        func() string
		expected string
	}{
		{puzzles.Euler1, "233168"},
		{puzzles.Euler2, "4613732"},
		{puzzles.Euler3, "6857"},
		{puzzles.Euler4, "906609"},
		{puzzles.Euler5, "232792560"},
		{puzzles.Euler6, "25164150"},
		{puzzles.Euler7, "104743"},
		{puzzles.Euler8, "23514624000"},
		{puzzles.Euler9, "31875000"},
		{puzzles.Euler10, "142913828922"},
		{puzzles.Euler11, "70600674"},
	}

	for _, tc := range cases {
		t.Run(utils.GetFuncName(tc.f), func(t *testing.T) {
			result := tc.f()
			if result != tc.expected {
				t.Fatalf("%v failed; got %v; expected %v",
					utils.GetFuncName(tc.f),
					result,
					tc.expected,
				)
			}
		})

	}
}
