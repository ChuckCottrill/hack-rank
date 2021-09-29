
// https://leetcode.com/problems/length-of-last-word/

class Solution {
public:
    int lengthOfLastWord(string s) {
        int size = s.size();
        int wordlen = 0;
        int last = size-1;
        for ( ; last >= 0; ) {
            if (s[last] == ' ') {
                last--;
            } else {
                break;
            }
        }
        for ( ; last >= 0; last-- ) {
            if (s[last]==' ') {
                break;
            }
            wordlen++;
        }
        return wordlen;
    }
};

