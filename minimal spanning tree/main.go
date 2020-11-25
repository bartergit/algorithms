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
	vertex := "a"
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
	fmt.Println("run tests pls")
	fmt.Println(Prim([]Edge{{"a", "b", 7}, {"c", "e", 5}, {"b", "c", 8}, {"a", "d", 5}, {"d", "e", 15}, {"d", "f", 6}, {"f", "g", 11}, {"e", "f", 8}, {"e", "g", 9}, {"b", "e", 7}, {"d", "b", 9}}, ))
}
