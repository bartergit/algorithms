package main

import (
	"testing"
)

var (
	testCases = [][]Edge{
		{{"a", "b", 7}, {"c", "e", 5}, {"b", "c", 8}, {"a", "d", 5}, {"d", "e", 15}, {"d", "f", 6}, {"f", "g", 11}, {"e", "f", 8}, {"e", "g", 9}, {"b", "e", 7}, {"d", "b", 9}},
		{{"a", "b", 2}, {"b", "d", 2}, {"a", "d", 1}, {"c", "d", 3}},
		{{"a", "b", 9}, {"a", "n", 2}, {"a", "h", 6}, {"a", "m", 4}, {"b", "c", 4}, {"b", "e", 7}, {"b", "f", 5}, {"b", "n", 9}, {"c", "d", 4}, {"c", "f", 1}, {"f", "d", 3}, {"f", "e", 9}, {"d", "e", 10}, {"g", "d", 18}, {"g", "e", 8}, {"g", "h", 9}, {"g", "m", 9}, {"h", "m", 3}, {"m", "e", 9}, {"n", "e", 8}, {"m", "n", 2}},
	}
	expected = []int{39, 6, 38}
)

func TestKruskal(t *testing.T) {
	for i := range testCases {
		tree := Kruskal(testCases[i])
		sum := 0
		for _, edge := range tree {
			sum += edge.w
		}
		if sum != expected[i] {
			t.Error(sum, expected[i])
		}
	}
}

func TestPrim(t *testing.T) {
	for i := range testCases {
		tree := Prim(testCases[i])
		sum := 0
		for _, edge := range tree {
			sum += edge.w
		}
		if sum != expected[i] {
			t.Error(sum, expected[i])
		}
	}
}
