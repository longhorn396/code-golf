package main

import (
	"errors"
	"fmt"
	"log"
	"os"
	"time"
)

func TempSwap(i int, j int) (int, int) {
	temp := i
	i = j
	j = temp
	return i, j
}

func Temp2Swap(i int, j int) (int, int) {
	temp := i
	i = j
	return i, temp
}

func TupleSwap(i int, j int) (int, int) {
	i, j = j, i
	return i, j
}

func ReturnSwap(i int, j int) (int, int) {
	return j, i
}

func XorSwap(i int, j int) (int, int) {
	i = i ^ j
	j = i ^ j
	i = i ^ j
	return i, j
}

func CompareSubfs(i int, j int) string {
	var attempts int
	var result string = ""
	subfs := map[string]func(i int, j int) (int, int){
		"temp":   TempSwap,
		"temp2":  Temp2Swap,
		"tuple":  TupleSwap,
		"return": ReturnSwap,
		"xor":    XorSwap,
	}
	fmt.Println("How many attempts?")
	fmt.Scanln(&attempts)
	for subfName, subf := range subfs {
		start := time.Now()
		for i := 0; i < attempts; i++ {
			_, _ = subf(i, j)
		}
		result += fmt.Sprintf("%s took %s\n", subfName, time.Since(start))
	}
	return result
}

func CompareWrapper(i int, j int) (int, int) {
	fmt.Print(CompareSubfs(i, j))
	return i, j
}

func main() {
	var i, j int
	var subf string
	subfs := map[string]func(i int, j int) (int, int){
		"temp":    TempSwap,
		"temp2":   Temp2Swap,
		"tuple":   TupleSwap,
		"return":  ReturnSwap,
		"xor":     XorSwap,
		"compare": CompareWrapper,
	}
	if len(os.Args) > 1 {
		subf = os.Args[1]
	} else {
		fmt.Println("What subfunction would you like to do?")
		fmt.Println("Options: temp, temp2, tuple, return, xor, compare")
		fmt.Scanln(&subf)
	}
	if f, ok := subfs[subf]; ok {
		if len(os.Args) > 3 {
			i, _ = fmt.Sscan(os.Args[2], &i)
			j, _ = fmt.Sscan(os.Args[3], &j)
		} else {
			fmt.Println("Enter two Integers:")
			fmt.Scanf("%d %d", &i, &j)
		}
		fmt.Print(f(i, j))
	} else {
		log.Fatal(errors.New("No matching subfunction for " + subf))
	}
}
