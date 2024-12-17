package hash

type hashConstraints interface {
	int | string
}

type HashTable[K hashConstraints, V comparable] struct {
	Index []K
	Data  []V
	Size  int
}

func Add[K hashConstraints, V comparable](table HashTable[K, V], key K, value V) {
	var index []K = table.Index
	var data []V = table.Data
	var size = table.Size
	switch k := any(key).(type) {
	case int:
		index[DoubleHashing[K](index, IntHash(k, size))] = key
		data[DoubleHashing[V](data, IntHash(k, size))] = value
	case string:
		index[DoubleHashing[K](index, StringHash(k, size))] = key
		data[DoubleHashing[V](data, StringHash(k, size))] = value
	}
}

func Search[K hashConstraints, V comparable](table HashTable[K, V], key K) (value V, found bool) {
	var emptyValue K
	var index []K = table.Index
	var data []V = table.Data
	var size = table.Size
	switch v := any(key).(type) {
	case int:
		k := IntHash(v, size)
		for index[k] != emptyValue {
			if index[k] == key {
				return data[k], true
			}
			k += IntHash2(v, size)
			k %= size
		}
	case string:
		k := StringHash(v, size)
		l := StringHash(v, size)
		for index[k] != emptyValue {
			if index[k] == key {
				return data[k], true
			}
			k += IntHash2(l, size)
			k %= size
		}
	}
	return value, false
}

func Update[K hashConstraints, V comparable](table HashTable[K, V], key K, value V) {
	var emptyValue K
	var index []K = table.Index
	var data []V = table.Data
	var size = table.Size
	switch v := any(key).(type) {
	case int:
		k := IntHash(v, size)
		for index[k] != emptyValue {
			if index[k] == key {
				data[k] = value
				break
			}
			k += IntHash2(v, size)
			k %= size
		}
	case string:
		k := StringHash(v, size)
		l := StringHash(v, size)
		for index[k] != emptyValue {
			if index[k] == key {
				data[k] = value
				break
			}
			k += IntHash2(l, size)
			k %= size
		}
	}
}

func Delete[K hashConstraints, V comparable](table HashTable[K, V], key K) {
	var emptyKey K
	var emptyValue V
	var index []K = table.Index
	var data []V = table.Data
	var size = table.Size
	switch v := any(key).(type) {
	case int:
		k := IntHash(v, size)
		for index[k] != emptyKey {
			if index[k] == key {
				data[k] = emptyValue
				index[k] = emptyKey
				break
			}
			k += IntHash2(v, size)
			k %= size
		}
	case string:
		k := StringHash(v, size)
		l := StringHash(v, size)
		for index[k] != emptyKey {
			if index[k] == key {
				data[k] = emptyValue
				index[k] = emptyKey
				break
			}
			k += IntHash2(l, size)
			k %= size
		}
	}
}
