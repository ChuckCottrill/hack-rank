
Reverse to Make Equal

'''

Reverse to Make Equal (Make Two Arrays Equal by Reversing Sub-arrays)
Given two arrays A and B of length N,
determine if there is a way to make A equal to B by reversing any subarrays from array B any number of times.
(In one step, you can select any non-empty sub-array of arr and reverse it. You are allowed to make any number of steps.)
Signature
bool areTheyEqual(int[] arr_a, int[] arr_b)
Input
All integers in array are in the range [0, 1,000,000,000].
Output
Return true if B can be made equal to A, return false otherwise.
Example
A = [1, 2, 3, 4]
B = [1, 4, 3, 2]
output = true
After reversing the subarray of B from indices 1 to 3, array B will equal array A.
'''

'''
Example 2:
Input: A = [1,2,3,4], B = [2,4,1,3]
Output: true
Explanation: You can follow the next steps to convert arr to target:
1- Reverse sub-array [2,4,1], arr becomes [1,4,2,3]
2- Reverse sub-array [4,2], arr becomes [1,2,4,3]
3- Reverse sub-array [4,3], arr becomes [1,2,3,4]
There are multiple ways to convert arr to target, this is not the only way to do so.
Example 2:

Input: A = [7], B = [7]
Output: true
Explanation: arr is equal to target without any reverses.
Example 3:

Input: A = [1,12], B = [12,1]
Output: true
Example 4:

Input: A = [3,7,9], B = [3,7,11]
Output: false
Explanation: arr doesn't have value 9 and it can never be converted to target.
Example 5:

Input: A = [1,1,1,1,1], B = [1,1,1,1,1]
Output: true
 

Constraints:

target.length == arr.length
1 <= target.length <= 1000
1 <= target[i] <= 1000
1 <= arr[i] <= 1000
'''

import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def are_they_equal(array_a, array_b):
  # Write your code here

# see https://leetcode.com/problems/pancake-sorting/

# hint:
# Each element of target should have a corresponding element in arr, and if it doesn't have a corresponding element, return false.
# hint:
# To solve it easily, sort the two arrays and check if they are equal.

def simple_solution(arr1,arr2):
    # a1 = arr1[:]
    # a2 = arr2[:]
    # a1 = list.copy(arr1)
    # a2 = list.copy(arr2)
    a1 = arr1.copy()
    a2 = arr2.copy()
    list.sort(a1)
    list.sort(a2)
    return a1 == a2

# step: reverse sublist
def flip(sublist,start,last):
    sublist[start:last] = reversed(sublist[start:last])
    print("reverse:",",".join([str(x) for x in sublist[start:last]]))
    return sublist

# boolean:
# def makeEqual(arr1, arr2):
def are_they_equal(array_a, array_b):
    """ sort by reversing sub-strings (like bubble-sort)
        reverse sublist containing needed number to head of list at each round/step
    """
    # arr1 = array_a
    # arr2 = array_b
    n = len(array_a)
    n2 = len(array_b)
    if n != n2: return False
    # print(array_b)
    ans = array_a[:]
    start = 0
    for ix,x in enumerate(array_a):
        # when already equal, nothing to do
        if array_b[ix] == x: continue
        # locate position of sublist to reverse this step
        try:
            pos = array_b.index(x,start,n2)
            print("x:",x,",at:",pos)
            flip(array_b,ix,pos+1)
            print(array_b)
        except:
            return False
    return array_a == array_b

  










# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom, but they are otherwise not editable!
def printString(string):
  print('[\"', string, '\"]', sep='', end='')

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
    printString(expected)
    print(' Your output: ', end='')
    printString(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  n_1 = 4
  a_1 = [1, 2, 3, 4]
  b_1 = [1, 4, 3, 2]
  expected_1 = True
  output_1 = are_they_equal(a_1, b_1)
  check(expected_1, output_1)

  n_2 = 4
  a_2 = [1, 2, 3, 4]
  b_2 = [1, 2, 3, 5]  
  expected_2 = False
  output_2 = are_they_equal(a_2, b_2)
  check(expected_2, output_2)

  # Add your own test cases here
  




