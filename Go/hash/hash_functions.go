package hash

func StringHash(key string, size int) int {
	g := 31
	hash_index := 0
	for c := range key {
		hash_index = (g*hash_index + c) % size
	}
	return hash_index
}

func IntHash(key int, size int) int {
	if size%2 == 0 {
		size -= 1
	}
	if key%size < 0 {
		key += size
	}
	return key % size
}

func IntHash2(key int, size int) int {
	if size%2 == 0 {
		size -= 1
	}
	if key%size < 0 {
		key += size
	}
	return size - (key % size)
}
