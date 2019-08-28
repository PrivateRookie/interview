package main

import (
	"fmt"
	"os"
)

func uniqueCharMap(s string) bool {
	charMap := make(map[int]int)
	for i := 0; i < len(s); i++ {
		ch := int(s[i])
		_, ok := charMap[ch]
		if ok {
			charMap[ch]++
		} else {
			charMap[ch] = 1
		}
	}
	unique := true
	for _, v := range charMap {
		if v > 1 {
			unique = false
			break
		}
	}
	return unique
}

func uniqueCharVec(s string) bool {
	var charVec [128]int
	unique := true
	for i := 0; i < len(s); i++ {
		ch := int(s[i])
		charVec[ch]++
		if charVec[ch] > 1 {
			unique = false
			break
		}
	}
	return unique
}

func main() {
	if uniqueCharMap("abdd") != false {
		os.Exit(1)
	} else {
		fmt.Println("Ok")
	}
	if uniqueCharMap("abcd") != true {
		os.Exit(1)
	} else {
		fmt.Println("Ok")
	}
	if uniqueCharVec("abdd") != false {
		os.Exit(1)
	} else {
		fmt.Println("Ok")
	}
	if uniqueCharVec("abcd") != true {
		os.Exit(1)
	} else {
		fmt.Println("Ok")
	}
}
