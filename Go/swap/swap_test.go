package main

import "testing"

func TestSwapping(t *testing.T) {
	i, j := 5641, 74351
	subfs := []func(i int, j int) (int, int){TempSwap, Temp2Swap, TupleSwap, ReturnSwap, XorSwap}
	for _, subf := range subfs {
		sj, si := subf(i, j)
		if si != i || sj != j {
			t.Fail()
		}
	}
}
