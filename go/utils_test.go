package main

import (
	"euler/utils"
	"fmt"
	"math"
	"reflect"
	"testing"
)

func TestPrimeFactors(t *testing.T) {
	cases := []struct {
		input    int
		expected map[int]int
	}{
		{0, map[int]int{}},
		{1, map[int]int{}},
		{2, map[int]int{2: 1}},
		{4, map[int]int{2: 2}},
		{6, map[int]int{2: 1, 3: 1}},
		{7, map[int]int{7: 1}},
		{8, map[int]int{2: 3}},
		{24, map[int]int{2: 3, 3: 1}},
		{25, map[int]int{5: 2}},
		{144, map[int]int{2: 4, 3: 2}},
	}

	for _, tc := range cases {
		name := fmt.Sprintf("number=%v", tc.input)
		t.Run(name, func(t *testing.T) {
			result := utils.PrimeFactors(tc.input)
			if !reflect.DeepEqual(result, tc.expected) {
				t.Fatalf(
					"%v failed; got %v; expected %v",
					name,
					result, tc.expected,
				)
			}

			// check the product of the factors == the input
			if len(result) != 0 {
				prod := 1
				for factor, power := range result {
					prod *= int(math.Pow(float64(factor), float64(power)))
				}
				if prod != tc.input {
					t.Fatalf(
						"%v fail: product of factors = %v; does not equal input number %v",
						name,
						prod,
						tc.input,
					)
				}
			}
		})
	}
}
func TestReverseString(t *testing.T) {
	cases := []struct {
		input    string
		expected string
	}{
		{"", ""},
		{"a", "a"},
		{"ab", "ba"},
		{"abba", "abba"},
		{"tacocat", "tacocat"},
		{"Robin", "niboR"},
		{"Hello!", "!olleH"},
	}

	for _, tc := range cases {
		t.Run(tc.input, func(t *testing.T) {
			result := utils.ReverseString(tc.input)
			if result != tc.expected {
				t.Fatalf(
					"%v failed; got %v; expected %v",
					tc.input,
					result, tc.expected,
				)
			}
		})
	}
}