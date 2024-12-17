package main

import (
	"algorithms/hash"
	"fmt"
)

func main() {
	var table hash.HashTable[string, int]
	table.Index = make([]string, 100)
	table.Data = make([]int, 100)
	table.Size = 100
	hash.Add(table, "hash", 12)
	hash.Add(table, "table", 1322)
	hash.Add(table, "map", 190)
	hash.Update(table, "map", 1234)
	fmt.Println(hash.Search(table, "table"))
	fmt.Println(hash.Search(table, "map"))
	hash.Delete(table, "map")
	fmt.Println(hash.Search(table, "map"))
}
