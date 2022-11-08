package utils

import (
	"fmt"
	"math"
	"os"
	"reflect"
	"runtime"
	"time"
)

func LoadPuzzleInput(filename string) string {
	path := fmt.Sprintf("../puzzle_inputs/%v.txt", filename)
	data, err := os.ReadFile(path)
	if err != nil {
		panic(err)
	}
	return string(data)
}

func GetFuncName(f func() string) string {
	return runtime.FuncForPC(reflect.ValueOf(f).Pointer()).Name()
}

func Profile(f func() string) string {
	// see also https://stackoverflow.com/questions/69759462/passing-an-arbitrary-function-as-a-parameter-in-go
	t1 := time.Now()
	result := f()
	t2 := time.Now()
	dt := float32(t2.UnixMicro()-t1.UnixMicro()) / 1000000
	message := fmt.Sprintf("%v: %v (%.5f seconds)",
		GetFuncName(f),
		result,
		dt,
	)
	fmt.Println(message)
	return result
}

func Assert(value string, expected string) {
	if value != expected {
		panic(fmt.Sprintf("AssertionError! \n\tgot:\t\t%v \n\texpected:\t%v", value, expected))
	}
}

func PrimeFactors(number int) map[int]int {
	factors := make(map[int]int)
	if number == 0 {
		return factors
	}
	remainder := number
	product := 1
	p := 2
	limit := int(math.Sqrt(float64(number)))
	for {
		if product == number {
			break
		}
		if p <= limit {
			for {
				if remainder%p != 0 {
					break
				}
				factors[p] += 1
				remainder = remainder / p
				product *= p
			}
			increment := 2
			if p%2 == 0 {
				increment = 1
			}
			p += increment
		} else if remainder != 1 {
			factors[remainder] += 1
			product *= remainder
		}
	}
	return factors
}

func ReverseString(str string) string {
	// todo: make this harder and less readable -.-
	byte_str := []rune(str)
	for i, j := 0, len(byte_str)-1; i < j; i, j = i+1, j-1 {
		byte_str[i], byte_str[j] = byte_str[j], byte_str[i]
	}
	return string(byte_str)
}

func MakeRange(start int, stop int) []int {
	descending := start > stop
	output := []int{}

	if descending {
		ii := 0
		n := start - 1
		for {
			if n < stop {
				break
			}
			output = append(output, n)
			ii++
			n--
		}
	} else {
		ii := 0
		n := start
		for {
			if n >= stop {
				break
			}
			output = append(output, n)
			ii++
			n++
		}
	}
	return output
}

func PrintAny(thing any) {
	fmt.Print(thing)
}
