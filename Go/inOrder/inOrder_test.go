package main

import (
	"strings"
	"testing"
)

var alphaWords = []string{"almost", "bit", "billowy", "biopsy"}
var alphaInput = strings.Join(alphaWords, " ")
var alphaResult = strings.Join(alphaWords, " - in order\n") + " - in order"
var nonAlphaWords = []string{"chef", "dig", "nope", "false"}
var nonAlphaInput = strings.Join(nonAlphaWords, " ")
var nonAlphaResult = strings.Join(nonAlphaWords, " - not in order\n") + " - not in order"

func HelpTestWordInOrder(t *testing.T, f func(word []rune) bool) {
	for _, alphaWord := range alphaWords {
		if !f([]rune(alphaWord)) {
			t.Fail()
		}
	}
	for _, nonAlphaWord := range nonAlphaWords {
		if f([]rune(nonAlphaWord)) {
			t.Fail()
		}
	}
}

func TestWordInOrderBranchPrediction(t *testing.T) {
	HelpTestWordInOrder(t, WordInOrderBranchPrediction)
}

func TestWordInOrderReadability(t *testing.T) {
	HelpTestWordInOrder(t, WordInOrderReadability)
}

func HelpTestInOrder(t *testing.T, f func(text string) string) {
	if f(alphaInput) != alphaResult {
		t.Fail()
	}
	if f(nonAlphaInput) != nonAlphaResult {
		t.Fail()
	}
}

func TestInOrderBranchPrediction(t *testing.T) {
	HelpTestInOrder(t, InOrderBranchPrediction)
}

func TestInOrderReadability(t *testing.T) {
	HelpTestInOrder(t, InOrderReadability)
}

func TestInOrderHeuristic(t *testing.T) {
	HelpTestInOrder(t, InOrderHeuristic)
}
