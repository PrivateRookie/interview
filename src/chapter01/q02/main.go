package main

import (
	"fmt"
	"os"
)

func reverseStr(s string) string {
	r := []rune(s)
	for i, j := 0, len(r)-2; i < j; i, j = i+1, j-1 {
		r[i], r[j] = r[j], r[i]
	}
	return string(r)
}

func main() {
	if reverseStr("abcd!") != "dcba!" {
		os.Exit(1)
	} else {
		fmt.Println("Ok")
	}
	if reverseStr("!") != "!" {
		os.Exit(1)
	} else {
		fmt.Println("Ok")
	}
}
