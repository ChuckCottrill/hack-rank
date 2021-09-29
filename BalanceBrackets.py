
Balance Brackets

### see: https://leetcode.com/discuss/interview-question/124551/

'''
Balance Brackets
A bracket is considered to be any one of the following characters: (, ), {, }, [, or ].
We consider two brackets to be matching if the first element is an open-bracket, e.g., (, {, or [, and the second bracket is a close-bracket of the same type, e.g., ( and ), [ and ], and { and } are the only pairs of matching brackets.
Furthermore, a sequence of brackets is said to be balanced if the following conditions are met:
The sequence is empty, or
The sequence is composed of two, non-empty, sequences both of which are balanced, or
The first and last brackets of the sequence are matching, and the portion of the sequence without the first and last elements is balanced.
You are given a string of brackets. Your task is to determine whether each sequence of brackets is balanced. If a string is balanced, return true, otherwise, return false
Signature
bool isBalanced(String s)
Input
String s with length between 1 and 1000
Output
A boolean representing if the string is balanced or not
Example 1
s = {[()]}
output: true
Example 2
s = {}()
output: true
Example 3
s = {(})
output: false
Example 4
s = )
output: false
'''

class Solution():
    def removeInvalidParentheses(self, str):
        if not str:
            return
        stack = []
        for ix, token in enumerate(str):
            print(token)
            if token == ")" and stack and stack[-1][1] == "(":
                stack.pop()
            elif token in ('(',')'):
                stack.append((ix,token))
            else:
                continue
            print(stack)
        #
        print(stack)
        str = list(str)
        while stack:
            # print(token)
            str.pop(stack.pop()[0])
        #
        return ''.join(str)

obj = Solution()
obj.removeInvalidParentheses("ab(a(c)fg)9)))") #== "ab(a(c)fg)9"
obj.removeInvalidParentheses(")a(b)c()(5") #== "a(b)c()5"
obj.removeInvalidParentheses(")(") #== ""
obj.removeInvalidParentheses("a(b))") #== "a(b)"

assert obj.removeInvalidParentheses("ab(a(c)fg)9)))") == "ab(a(c)fg)9"
assert obj.removeInvalidParentheses(")a(b)c()(5") == "a(b)c()5"
assert obj.removeInvalidParentheses(")(") == ""
assert obj.removeInvalidParentheses("a(b))") == "a(b)"


import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def isBalanced(s):
  # Write your code here
  if not s:
    return False
  matchbeg = { "(":")", "{":"}", "[":"]" }
  matchend = { ")":"(", "}":"{", "]":"[" }
  stack = []
  for ix, token in enumerate(s):
    # print(token)
    if token in matchbeg: # ( '(', '{', '[' ):
      # print("push:",token)
      stack.append(token)
    elif token in matchend: # ( ')', '}', ']' ):
      if stack and stack[-1] == matchend[token]:
        val = stack.pop()
        # print("pop:",val)
      else:
        print("expect:",matchend[token])
        return False
    else:
      continue
    # print stack
  # print stack
  return len(stack) == 0

isBalanced("{[(])}")
isBalanced("{{[[(())]]}}")

def removeInvalidParentheses(self, str):
  if not str:
    return
  stack = []
  for ix, token in enumerate(str):
    print(token)
    if token == ")" and stack and stack[-1][1] == "(":
      stack.pop()
    elif token in ('(',')'):
      stack.append((ix,token))
    else:
      continue
    print(stack)
  #
  print(stack)
  str = list(str)
  while stack:
    # print(token)
    str.pop(stack.pop()[0])
  #
  return ''.join(str)

