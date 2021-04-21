package main

import (
	"fmt"
	"sort"
)

type Edge struct {
	a, b interface{}
	w    int
}

func Kruskal(edges []Edge) (tree []Edge) {
	sort.SliceStable(edges, func(i, j int) bool { return edges[i].w > edges[j].w })
	components := map[interface{}]int{}
	for _, edge := range edges {
		if components[edge.a] == 0 {
			components[edge.a] = len(components) + 1
		}
		if components[edge.b] == 0 {
			components[edge.b] = len(components) + 1
		}
	}
	changeComponents := func(fromVertex, toVertex interface{}) {
		componentFrom := components[fromVertex]
		componentTo := components[toVertex]
		for vertex, component := range components {
			if component == componentFrom {
				components[vertex] = componentTo
			}
		}
	}
	for i := 0; i < len(components) - 1; i++ {
		for _ = range edges {
			toAppend := edges[len(edges)-1]
			edges = edges[:len(edges)-1]
			if components[toAppend.a] != components[toAppend.b] {
				tree = append(tree, toAppend)
				changeComponents(toAppend.a, toAppend.b)
				break
			}
		}
	}
	return
}

func Prim(edges []Edge) (tree []Edge) {
	sort.SliceStable(edges, func(i, j int) bool { return edges[i].w < edges[j].w })
	visited := map[interface{}]bool {}
	for _, edge := range edges {
		visited[edge.a], visited[edge.b] = false, false
	}
	vertex := "1"
	visited[vertex] = true
	for i := 0; i < len(visited) - 1; i++ {
		for _, edge := range edges {
			if visited[edge.a] != visited[edge.b] {  //xor
				visited[edge.a] = true
				visited[edge.b] = true
				tree = append(tree, edge)
				break
			}
		}
	}
	return
}

func main() {
	s:= Prim([]Edge{{"1", "16", 6}, {"2", "8", 1}, {"2", "3", 1}, {"2", "11", 3}, {"2", "7", 1}, {"2", "12", 6}, {"2", "5", 5}, {"3", "15", 6}, {"4", "15", 4}, {"5", "13", 6}, {"6", "9", 5}, {"6", "7", 6}, {"6", "8", 2}, {"7", "10", 6}, {"7", "16", 2}, {"7", "11", 6}, {"9", "14", 3}, {"10", "14", 6}, {"12", "14", 6}, {"12", "13", 4}, {"14", "15", 6}})
	fmt.Println(s)
	sum:=0
	for i := 0; i < len(s); i++ {
		sum += s[i].w
	}
	fmt.Println(sum)
}
