
# https://stackoverflow.com/questions/8899905/count-number-of-occurrences-of-a-substring-in-a-string
# https://www.geeksforgeeks.org/number-substrings-string/

def count_substring(string, sub_string):
    k=len(string)
    m=len(sub_string)
    i=0
    l=0
    count=0
    while l<k:
        if string[l:l+m]==sub_string:
            count=count+1
        l=l+1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)

# https://www.techiedelight.com/find-longest-substring-given-string-containing-distinct-characters/

# Function to find the longest substring with all
# distinct characters using a sliding window
def findLongestSubstringing(str):
 
    # mark characters present in the current window
    window = {}
 
    # stores the longest substring boundaries
    begin = end = 0
 
    # `[low…high]` maintain the sliding window boundaries
    low = high = 0
 
    while high < len(str):
 
        # if the current character is present in the current window
        if window.get(str[high]):
 
            # remove characters from the left of the window till
            # we encounter the current character
            while str[low] != str[high]:
                window[str[low]] = False
                low = low + 1
 
            low = low + 1        # remove the current character
        else:
            # if the current character is not present in the current
            # window, include it
            window[str[high]] = True
 
            # update the maximum window size if necessary
            if end - begin < high - low:
                begin = low
                end = high
 
        high = high + 1
 
    # return the longest substring found at `str[begin…end]`
    return str[begin:end + 1]
 
 
if __name__ == '__main__':
 
    str = "abbcdafeegh"
    print(findLongestSubstringing(str))

# https://www.geeksforgeeks.org/length-of-the-longest-substring-without-repeating-characters/
# https://www.geeksforgeeks.org/print-longest-substring-without-repeating-characters/

Method 3 (Linear Time): Let us talk about the linear time solution now. This solution uses extra space to store the last indexes of already visited characters. The idea is to scan the string from left to right, keep track of the maximum length Non-Repeating Character Substring seen so far in res. When we traverse the string, to know the length of current window we need two indexes.
1) Ending index ( j ) : We consider current index as ending index.
2) Starting index ( i ) : It is same as previous window if current character was not present in the previous window. To check if the current character was present in the previous window or not, we store last index of every character in an array lasIndex[]. If lastIndex[str[j]] + 1 is more than previous start, then we updated the start index i. Else we keep same i.

Below is the implementation of the above approach :

# Python3 program to find the length
# of the longest substring
# without repeating characters
def longestUniqueSubsttr(string):
 
    # last index of every character
    last_idx = {}
    max_len = 0
 
    # starting index of current
    # window to calculate max_len
    start_idx = 0
 
    for i in range(0, len(string)):
       
        # Find the last index of str[i]
        # Update start_idx (starting index of current window)
        # as maximum of current value of start_idx and last
        # index plus 1
        if string[i] in last_idx:
            start_idx = max(start_idx, last_idx[string[i]] + 1)
 
        # Update result if we get a larger window
        max_len = max(max_len, i-start_idx + 1)
 
        # Update last index of current char.
        last_idx[string[i]] = i
 
    return max_len
 
 
# Driver program to test the above function
string = "geeksforgeeks"
print("The input string is " + string)
length = longestUniqueSubsttr(string)
print("The length of the longest non-repeating character" +
      " substring is " + str(length))


# Python3 program to find and print longest
# substring without repeating characters.
 
# Function to find and print longest
# substring without repeating characters.
def findLongestSubstring(string):
 
    n = len(string)
 
    # starting point of current substring.
    st = 0
 
    # maximum length substring without
    # repeating characters.
    maxlen = 0
 
    # starting index of maximum
    # length substring.
    start = 0
 
    # Hash Map to store last occurrence
    # of each already visited character.
    pos = {}
 
    # Last occurrence of first
    # character is index 0
    pos[string[0]] = 0
 
    for i in range(1, n):
 
        # If this character is not present in hash,
        # then this is first occurrence of this
        # character, store this in hash.
        if string[i] not in pos:
            pos[string[i]] = i
 
        else:
            # If this character is present in hash then
            # this character has previous occurrence,
            # check if that occurrence is before or after
            # starting point of current substring.
            if pos[string[i]] >= st:
 
                # find length of current substring and
                # update maxlen and start accordingly.
                currlen = i - st
                if maxlen < currlen:
                    maxlen = currlen
                    start = st
 
                # Next substring will start after the last
                # occurrence of current character to avoid
                # its repetition.
                st = pos[string[i]] + 1
             
            # Update last occurrence of
            # current character.
            pos[string[i]] = i
         
    # Compare length of last substring with maxlen
    # and update maxlen and start accordingly.
    if maxlen < i - st:
        maxlen = i - st
        start = st
     
    # The required longest substring without
    # repeating characters is from string[start]
    # to string[start+maxlen-1].
    return string[start : start + maxlen]
 
# Driver Code
if __name__ == "__main__":
 
    string = "GEEKSFORGEEKS"
    print(findLongestSubstring(string))
 
# This code is contributed by Rituraj Jain



