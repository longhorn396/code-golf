package main

import (
	"bufio"
	"errors"
	"fmt"
	"log"
	"os"
	"strings"
	"time"
)

func InOrder(text string, f func(word []rune) bool) string {
	words := strings.Split(strings.ToLower(text), " ")
	var results []string
	for _, word := range words {
		order := f([]rune(word))
		var verdict string
		if order {
			verdict = ""
		} else {
			verdict = "not "
		}
		results = append(results, fmt.Sprintf("%v - %vin order", word, verdict))
	}
	return strings.Join(results, "\n")
}

func InOrderBranchPrediction(text string) string {
	return InOrder(text, WordInOrderBranchPrediction)
}

func InOrderReadability(text string) string {
	return InOrder(text, WordInOrderReadability)
}

func InOrderHeuristic(text string) string {
	words := strings.Split(strings.ToLower(text), " ")
	var results []string
	for _, word := range words {
		var order bool
		if word[0] > 'm' {
			order = WordInOrderReadability([]rune(word))
		} else {
			order = WordInOrderBranchPrediction([]rune(word))
		}
		var verdict string
		if order {
			verdict = ""
		} else {
			verdict = "not "
		}
		results = append(results, fmt.Sprintf("%v - %vin order", word, verdict))
	}
	return strings.Join(results, "\n")
}

func WordInOrderBranchPrediction(word []rune) bool {
	for i, character := range word[:len(word)-1] {
		if character <= word[i+1] {
			continue
		}
		return false
	}
	return true
}

func WordInOrderReadability(word []rune) bool {
	for i, character := range word[:len(word)-1] {
		if character > word[i+1] {
			return false
		}
	}
	return true
}

func CompareSubfs(text string) string {
	var attempts int
	var result string = ""
	subfs := map[string]func(text string) string{
		"branchPrediction": InOrderBranchPrediction,
		"readability":      InOrderReadability,
		"heuristic":        InOrderHeuristic,
	}
	fmt.Println("How many attempts?")
	fmt.Scanln(&attempts)
	for subfName, subf := range subfs {
		start := time.Now()
		for i := 0; i < attempts; i++ {
			_ = subf(text)
		}
		result += fmt.Sprintf("%s took %s\n", subfName, time.Since(start))
	}
	return result
}

func main() {
	var subf, text string
	subfs := map[string]func(text string) string{
		"branchPrediction": InOrderBranchPrediction,
		"readability":      InOrderReadability,
		"heuristic":        InOrderHeuristic,
		"compare":          CompareSubfs,
	}
	if len(os.Args) > 1 {
		subf = os.Args[1]
	} else {
		fmt.Println("What subfunction would you like to do?")
		fmt.Println("Options: branchPrediction, readability, heuristic, compare")
		fmt.Scanln(&subf)
	}
	if f, ok := subfs[subf]; ok {
		if len(os.Args) > 2 {
			text = os.Args[2]
		} else {
			fmt.Println("What word(s)?")
			text, _ = bufio.NewReader(os.Stdin).ReadString('\n')
			text = text[:len(text)-1]
		}
		fmt.Print(f(text))
	} else {
		log.Fatal(errors.New("No matching subfunction for " + subf))
	}
}
