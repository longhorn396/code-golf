package main

import (
	"fmt"
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
	fmt.Println(InOrderBranchPrediction("almost chef"))
	fmt.Println(InOrderReadability("bit dig"))
	fmt.Println(InOrderHeuristic("billowy nope"))
}
