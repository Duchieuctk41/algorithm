import (
    "strings"
)

func canConstruct(ransomNote string, magazine string) bool {
	vocab := map[rune]int{}

	for _, index := range magazine {
		vocab[index]++
	}

	for _, letter := range ransomNote {
		if vocab[letter] == 0 {
			return false
		}
		vocab[letter]--
	}
	return true
}

func canConstruct(ransomNote string, magazine string) bool {
	byteIndex := make([]int, 26)
	for _, letter := range magazine {
		byteIndex[int(letter-'a')]++
	}
	for _, letter := range ransomNote {
		byteIndex[int(letter-'a')]--
	}

	for i := range byteIndex {
		if byteIndex[i] < 0 {
			return false
		}
	}
	return true
}

// Input: ransomNote = "a", magazine = "b"
// Output: false

// Input: ransomNote = "aa", magazine = "aab"
// Output: true

// Input: ransomNote = "aa", magazine = "ab"
// Output: false