

Slow Sums

### see: https://leetcode.com/discuss/interview-question/590101/facebook-interview-question-slow-sum

'''
Slow Sums
Suppose we have a list of N numbers,
and repeat the following operation until we are left with only a single number:
    Choose any two numbers and replace them with their sum.
    Moreover, we associate a penalty with each operation equal to the value of the new number,
    and call the penalty for the entire list as the sum of the penalties of each operation.
For example, given the list [1, 2, 3, 4, 5],
we could choose 2 and 3 for the first operation,
which would transform the list into [1, 5, 4, 5] and incur a penalty of 5.
The goal in this problem is to find the worst possible penalty for a given input.
Signature:
int getTotalTime(int[] arr)
Input:
An array arr containing N integers, denoting the numbers in the list.
Output format:
An int representing the worst possible total penalty.
Constraints:
1 ≤ N ≤ 10^6
1 ≤ Ai ≤ 10^7, where *Ai denotes the ith initial element of an array.
The sum of values of N over all test cases will not exceed 5 * 10^6.
Example
arr = [4, 2, 1, 3]
output = 26
First, add 4 + 3 for a penalty of 7. Now the array is [7, 2, 1]
Add 7 + 2 for a penalty of 9. Now the array is [9, 1]
Add 9 + 1 for a penalty of 10. The penalties sum to 26.
'''

'''
Slow Sums
Suppose we have a list of N numbers, Choose any two adjacent numbers and replace them with their sum. Lets call the value of the new number as "cost".
Repeat the following operation until we're left with only a single number and add costs for each "merge" operation.
The goal of the problem is to find the "max cost" possible for a given input.

For example, given the list [1, 2, 3, 4, 5], we could choose 4 and 5 for the first operation, which would transform the list into [1, 2, 3, 9] and incur a cost of 9.
Signature:
int getTotalTime(int[] arr)
Input:
An array arr containing N integers, denoting the numbers in the list.
Output format:
An int representing the max cost.
Constraints:
1 ≤ N ≤ 106
1 ≤ Ai ≤ 107, where *Ai denotes the ith initial element of an array.
The sum of values of N over all test cases will not exceed 5 * 106.
Example
arr = [4, 2, 1, 3]
output = 23
First, add 4 + 2 for a cost of 6. Now the array is [6, 1, 3]
Add 6 + 1 for a cost of 7. Now the array is [7, 3]
Add 7 + 3 for a cost of 10. The costs sum to 23.

arr_2 = [2, 3, 9, 8, 4]
output = 88
'''

import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def getTotalTime(arr):
  # Write your code here
  arr.sort()
  penalty = []
  while len(arr) > 1:
    # a1,a2 = arr[-1],arr[-2]
    a1 = arr.pop()
    a2 = arr.pop()
    # penalty = a1+a2
    arr.append(a1+a2)
    penalty.append(a1+a2)
  print(penalty)
  return sum(penalty)

# getTotalTime([4, 2, 1, 3])
# getTotalTime([2, 3, 9, 8, 4])
  
  









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
  arr_1 = [4, 2, 1, 3]
  expected_1 = 26
  output_1 = getTotalTime(arr_1)
  check(expected_1, output_1)

  arr_2 = [2, 3, 9, 8, 4]
  expected_2 = 88
  output_2 = getTotalTime(arr_2)
  check(expected_2, output_2)

  # Add your own test cases here
  

