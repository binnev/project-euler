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

	ii := 0
	if descending {
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

func IntPow(number int, exponent int) int {
	return int(math.Pow(
		float64(number),
		float64(exponent),
	))
}

func Sum(iterable []int) int {
	total := 0
	for _, value := range iterable {
		total += value
	}
	return total
}

func Map(f func(int) int, iterable []int) []int {
	output := make([]int, len(iterable))
	for ii, value := range iterable {
		output[ii] = f(value)
	}
	return output
}

func PrintAny(thing ...any) {
	// so this IS possible!
	fmt.Println(thing...)
}

func PrintType(x any) {
	fmt.Println(reflect.TypeOf(x).String())
}

func DetectType(x any) string {
	switch x.(type) {
	case string:
		return "string!"
	case int:
		return "int!"
	case float64:
		return "float64!"
	default:
		return "dunno!"
	}
}

// Eratosthenes' Sieve
func SievePrimes(limit int) []int {
	if limit < 2 {
		return []int{}
	}
	primes := []int{2}
	composites := map[int]bool{}
	for n := 3; n < limit+1; n += 2 {
		if !composites[n] {
			primes = append(primes, n)
			for c := IntPow(n, 2); c < limit; c += n {
				composites[c] = true
			}
		}
	}
	return primes
}

func MaxInt(numbers []int) int {
	biggest := 0
	for _, value := range numbers {
		if value > biggest {
			biggest = value
		}
	}
	return biggest
}

func ProductInt(numbers []int) int {
	prod := 1
	for _, value := range numbers {
		prod *= value
	}
	return prod
}
