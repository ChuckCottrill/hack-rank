


Passing Yearbooks

'''
Passing Yearbooks
There are n students, numbered from 1 to n, each with their own yearbook.
They would like to pass their yearbooks around and get them signed by other students.
You are given a list of n integers arr[1..n], which is guaranteed to be a permutation of 1..n
    (in other words, it includes the integers from 1 to n exactly once each, in some order).
The meaning of this list is described below.
Initially, each student is holding their own yearbook.
    The students will then repeat the following two steps each minute:
    Each student i first signs the yearbook that they are currently holding (which may either belong to themselves or to another student),
    and then student passes yearbook to student arr[i-1].
It is possible that arr[i-1] = i for any given i, in which case student i will pass their yearbook back to themselves.
Once a student has received their own yearbook back, they will hold on to it and no longer participate in the passing process.
*** and then student passes yearbook to student arr[i]
*** It is possible that arr[i] = i for any given i, in which case student i will pass their yearbook back to themselves.
It is guaranteed that, for any possible valid input,
each student will eventually receive their own yearbook back and will never end up holding more than one yearbook at a time.
Compute a list of n integers output,
whose element at i-1 is equal to the number of signatures that will be present in student i's yearbook once they receive it back.

Signature
int[] findSignatureCounts(int[] arr)
Input
n is in the range [1, 100,000].
Each value arr[i] is in the range [1, n], and all values in arr[i] are distinct.
Output
Return a list of n integers output, as described above.

Example 1
n = 2
arr = [2, 1]
output = [2, 2]
Pass 1:
Student 1 signs their own yearbook. Then they pass the book to the student at arr[0], which is Student 2.
Student 2 signs their own yearbook. Then they pass the book to the student at arr[1], which is Student 1.
Pass 2:
Student 1 signs Student 2's yearbook. Then they pass it to the student at arr[0], which is Student 2.
Student 2 signs Student 1's yearbook. Then they pass it to the student at arr[1], which is Student 1.
Pass 3:
Both students now hold their own yearbook, so the process is complete.
Each student received 2 signatures.
...  resulting in 2 signatures each.

Example 2
n = 2
arr = [1, 2]
output = [1, 1]
Pass 1:
Student 1 signs their own yearbook. Then they pass the book to the student at arr[0], which is themself, Student 1.
Student 2 signs their own yearbook. Then they pass the book to the student at arr[1], which is themself, Student 2.
...  resulting in 1 signature each.
Pass 2:
Both students now hold their own yearbook, so the process is complete.
Each student received 1 signature.
'''


import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


# recognize that there may be 1 to n cycles
def findSignatureCounts(arr):
  # Write your code here
  n = len(arr)
  visited_students = [False] * (n+1)
  signatures = [0] * n
  cycle_indexes = [-1] * n
  # for each student
  for ix in range(len(arr)):
    student = arr[ix]
    print("student:",student)
    # avoid traversing cycle more than once
    if visited_students[student]:
      print("visited:",student)
      continue
    visited_students[student] = True
    print("visit:",student)
    # sign own yearbook
    signatures[ix] = 1
    # consider current student root of a cycle, traverse cycle
    link = student - 1
    #
    print("link:",link)
    ### count = 0
    # increment prior to loop?
    cycle_indexes[link] = ix
    while link != ix:
      signatures[ix] += 1
      # increment here? or prior to loop? or both?
      cycle_indexes[link] = ix
      visited_students[arr[link]] = True
      print("  visit:",arr[link])
      link = arr[link] - 1
      #
      print("  link:",link)
      ### if count > 10: break
  print(signatures)
  # return the signature counts for each root nodes, and the referenced root node counts of traversed nodes
  for ix in range(len(arr)):
    if cycle_indexes[ix] != -1:
      signatures[ix] = signatures[cycle_indexes[ix]]
  return signatures

findSignatureCounts([2,1])
findSignatureCounts([1,2])
findSignatureCounts([3,2,1,4])
findSignatureCounts([1,2,3,4])
findSignatureCounts([1,2,3,4,5])
findSignatureCounts([4,3,2,1])
findSignatureCounts([2,3,4,5,1])
...
  
  









# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom, but they are otherwise not editable!

def printInteger(n):
  print('[', n, ']', sep='', end='')

def printIntegerList(array):
  size = len(array)
  print('[', end='')
  for i in range(size):
    if i != 0:
      print(', ', end='')
    print(array[i], end='')
  print(']', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  expected_size = len(expected)
  output_size = len(output)
  result = True
  if expected_size != output_size:
    result = False
  for i in range(min(expected_size, output_size)):
    result &= (output[i] == expected[i])
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printIntegerList(expected)
    print(' Your output: ', end='')
    printIntegerList(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  arr_1 = [2, 1]
  expected_1 = [2, 2]
  output_1 = findSignatureCounts(arr_1)
  check(expected_1, output_1)

  arr_2 = [1, 2]
  expected_2 = [1, 1]
  output_2 = findSignatureCounts(arr_2)
  check(expected_2, output_2)


  # Add your own test cases here
  



