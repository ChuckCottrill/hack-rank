
Pair Sums

'''
Pair Sums
Given a list of n integers arr[0..(n-1)], determine the number of different pairs of elements within it which sum to k.
If an integer appears in the list multiple times, each copy is considered to be different; that is, two pairs are considered different if one pair includes at least one array index which the other doesn't, even if they include the same values.
Signature
int numberOfWays(int[] arr, int k)
Input
n is in the range [1, 100,000].
Each value arr[i] is in the range [1, 1,000,000,000].
k is in the range [1, 1,000,000,000].
Output
Return the number of different pairs of elements which sum to k.
Example 1
n = 5
k = 6
arr = [1, 2, 3, 4, 3]
output = 2
The valid pairs are 2+4 and 3+3.
Example 2
n = 5
k = 6
arr = [1, 5, 3, 3, 3]
output = 4
There's one valid pair 1+5, and three different valid pairs 3+3 (the 3rd and 4th elements, 3rd and 5th elements, and 4th and 5th elements).
'''

import math
# Add any extra import statements you may need here

# Add any helper functions you may need here

def numberOfWaysSimple(arr, k):
  # Write your code here
  count = 0
  # for idx in range(len(arr)):
  #   match[arr[idx]] = []
  for ix in range(len(arr)):
    for iy in range(ix+1,len(arr)):
      if arr[ix]+arr[iy] == k:
        count += 1
  return count

def numberOfWays(arr, k):
  # Write your code here
  count = 0
  paired = []
  match = {}
  # create map to match with other element (not itself)
  for ix,x in enumerate(arr):
    if not x in match:
      match[x] = []
    match[x].append(ix)
  for iy,y in enumerate(arr):
    # pair, k = x+y, x = k-y
    if k-y in match:
      for ix in match[k-y]:
        # skip itself
        if ix == iy: continue
        # print("[{}]{} + [{}]{} = {}".format(ix,arr[ix],iy,arr[iy],k))
        paired.append( (arr[ix],y) )
        count += 1
  # print(paired)
  # print(count/2)
  return int(count/2)

# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom, but they are otherwise not editable!

def printInteger(n):
  print('[', n, ']', sep='', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  result = False
  if expected == output:
    result = True
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printInteger(expected)
    print(' Your output: ', end='')
    printInteger(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  k_1 = 6
  arr_1 = [1, 2, 3, 4, 3]
  expected_1 = 2
  output_1 = numberOfWays(arr_1, k_1)
  check(expected_1, output_1)

  k_2 = 6
  arr_2 = [1, 5, 3, 3, 3]
  expected_2 = 4
  output_2 = numberOfWays(arr_2, k_2)
  check(expected_2, output_2)

  # Add your own test cases here


