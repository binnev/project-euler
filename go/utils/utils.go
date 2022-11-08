package utils

import (
	"fmt"
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
	...
}
