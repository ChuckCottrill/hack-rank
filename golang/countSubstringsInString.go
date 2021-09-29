
package main

import {
    "fmt"
}

// https://stackoverflow.com/questions/8899905/count-number-of-occurrences-of-a-substring-in-a-string
// https://www.geeksforgeeks.org/number-substrings-string/
// https://www.techiedelight.com/find-longest-substring-given-string-containing-distinct-characters/
// Function to find the longest substring with all
// distinct characters using a sliding window
// https://www.geeksforgeeks.org/length-of-the-longest-substring-without-repeating-characters/
// https://www.geeksforgeeks.org/print-longest-substring-without-repeating-characters/

/*
Method 3 (Linear Time): Let us talk about the linear time solution now. This solution uses extra space to store the last indexes of already visited characters. The idea is to scan the string from left to right, keep track of the maximum length Non-Repeating Character Substring seen so far in res. When we traverse the string, to know the length of current window we need two indexes. 
1) Ending index ( j ) : We consider current index as ending index. 
2) Starting index ( i ) : It is same as previous window if current character was not present in the previous window. To check if the current character was present in the previous window or not, we store last index of every character in an array lasIndex[]. If lastIndex[str[j]] + 1 is more than previous start, then we updated the start index i. Else we keep same i.  

Below is the implementation of the above approach :
*/

// find the length of the longest substring without repeating characters

// find and print longest substring without repeating characters
func findLongestSubstring(s string) string {

    N := len(s)
    if N == 0 {
        return s
        // return 0
    }

    // store position where character last seen
    var seen = make(map[rune]int)
// var count = make(map[rune]int) // Where to store characters

    // maximum length substring without repeating characters
    var maxlen int

    // start index of maximum length substring
    start := 0
    left := 0

    for k,v := range s {
        if val, ok := seen[v]; ok {
            if left < val {
                left = val
            }
        }
        if max < k - left + 1 {
            max = k - left + 1
            start = left
        }
        seen[v] = k + 1 // update position seen
    }

    // fmt.Println(s[start:start+max])
    return str[start : start + maxlen]
    // return maxlen
}

func main() {
    str = "GEEKSFORGEEKS"
    print(findLongestSubstring(str));
}


