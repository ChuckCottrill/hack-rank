
// https://leetcode.com/problems/length-of-last-word/

func lengthOfLastWord(s string) int {
    var size int = len(s)
    var last int
    var wordlen int
    for last = size-1; last >= 0; {
        if s[last] != ' ' {
	    break
        }
        last--
    }
    for ; last >= 0; last-- {
        if s[last] == ' ' {
	    break
        }
        wordlen++
    }
    return wordlen
}
