package main

import (
	"fmt"
	"log"
	"longhorn396/gocg"
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
	subfs := map[string]func(i int, j int) (int, int){
		"temp":    TempSwap,
		"temp2":   Temp2Swap,
		"tuple":   TupleSwap,
		"return":  ReturnSwap,
		"xor":     XorSwap,
		"compare": CompareWrapper,
	}
	subf, err := gocg.FindSubf(subfs)
	if err == nil {
		var i, j int
		if len(os.Args) > 3 {
			fmt.Sscan(os.Args[2], &i)
			fmt.Sscan(os.Args[3], &j)
		} else {
			fmt.Println("Enter two Integers:")
			fmt.Scanf("%d %d", &i, &j)
		}
		fmt.Print(subfs[subf](i, j))
	} else {
		log.Fatal(err)
	}
}
