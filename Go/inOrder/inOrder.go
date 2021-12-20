package main

import (
	"bufio"
	"errors"
	"fmt"
	"log"
	"os"
	"strings"
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

func main() {
	var subf, text string
	subfs := map[string]func(text string) string{
		"branchPrediction": InOrderBranchPrediction,
		"readability":      InOrderReadability,
		"heuristic":        InOrderHeuristic,
	}
	if len(os.Args) > 1 {
		subf = os.Args[1]
	} else {
		fmt.Println("What subfunction would you like to do?")
		fmt.Println("Options: branchPrediction, readability, heuristic, compare")
		fmt.Scanln(&subf)
	}
	if len(os.Args) > 2 {
		text = os.Args[2]
	} else {
		fmt.Println("What word(s)?")
		text, _ = bufio.NewReader(os.Stdin).ReadString('\n')
		text = text[:len(text)-1]
	}
	if f, ok := subfs[subf]; ok {
		fmt.Print(f(text))
	} else {
		log.Fatal(errors.New("No matching subfunction for " + subf))
	}
}
