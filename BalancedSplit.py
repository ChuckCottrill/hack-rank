
'''
Balanced Split
Given a set of integers (which may include repeated integers),
determine if there exists a way to split the set into two subsets A and B,
    such that the sum of the integers in both sets is the same,
    and all of the integers in A are strictly smaller than all of the integers in B.
Note: Strictly smaller denotes that every integer in A must be less than, and not equal to, every integer in B.
Signature
bool balancedSplitExists(int[] arr)
Input
All integers in array are in the range [0, 1,000,000,000].
Output
Return true if such a split is possible, and false otherwise.

*Example 1
arr = [1, 5, 7, 1]
output = true
We can split the set into A = {1, 1, 5} and B = {7}.
*

Example 2
arr = [12, 7, 6, 7, 6]
output = false
We can't split the set into A = {6, 6, 7} and B = {7, 12} since this doesn't satisfy the requirement that all
integers in A are smaller than all integers in B.*
'''

def balancedSplitExists(arr):
    if not arr:
        return False
    target = sum(arr)
    if target % 2 != 0:
        return False
    target /= 2
    #
    def canSplit(cur_arr, lo_sum):
        if not cur_arr:
            return False
        pivot = cur_arr[0]
        s, lo, hi = 0, [], []
        for x in cur_arr:
            if x < pivot:
                s += x
                lo.append(x)
            elif x == pivot:
                s += x
            else:
                hi.append(x)
        if target == s + lo_sum:
            return True
        # elif s < target:
        elif s + lo_sum < target:
            return canSplit(hi, s + lo_sum)
        else:
            return canSplit(lo, lo_sum)
        return canSplit(arr, 0)

n = 10000
arr = list(range(n)) + [sum(range(n))]
random.shuffle(arr)
tests = [
        [[1, 5, 7, 1], True],
        # [[12, 7, 6, 7, 6], False],
        [[12, 7, 6, 7, 6], True],
        [[], False],
        [[2], False],
        [[20, 2], False],
        [[5,7,20,12,5,7,6,14,5,5,6], True],
        [[5,7,20,12,5,7,6,7,14,5,5,6], False],
        # [[1,1,1,1,1,1,1,1,1,1,1,1], False],
        [[1,1,1,1,1,1,1,1,1,1,1,1], True],
        [arr, True],
        ]

for test, ans in tests:
    print(balancedSplitExists(test), ans)


# split array into Two equal sum subarrays
# return split index
# when not possible, return -1
def findSplitPoint(arr, n) :
    # traverse array, compute left sum
    leftSum = 0
    for ix in range(0, n):
        leftSum += arr[ix]
    #
    # traverse array, compute right sum
    # check whether leftSum equal rightSum
    rightSum = 0
    for ix in range(n-1, -1, -1):
        rightSum += arr[ix]
        # remove current element from leftSum
        leftSum -= arr[ix]
        if (rightSum == leftSum):
            return ix
    # when not possible to split array into two equal parts
    return -1
  
# find split point, then print two parts
def printTwoParts(arr, n):
    arr.sort()
    splitPoint = findSplitPoint(arr, n)
    if (splitPoint < 0 or splitPoint == n ):
        # print ("Not Possible")
        return False
    # for ix in range (0, n):
    #     if(splitPoint == ix):
    #         print ("")
    #     print (arr[ix], end = " ")        
    return True

for test, ans in tests:
    print(printTwoParts(test,len(test)), ans)
  
# Driver Code
arr = [1, 2, 3, 4, 5, 5]
n = len(arr)
printTwoParts(arr, n)
  
# This code is contributed by Manish Shaw
# (manishshaw1)


# doesn't work - fails at marked line
def quickSelect(arr):
    m = min(arr)
    #
    i = 0
    while i < len(arr) and arr[i] == m:
        i += 1
    #
    if i == len(arr):
        return 0, len(arr)
    #
    temp = arr[i]
    arr[i] = arr[0]
    arr[0] = temp
    #
    pivot = arr[0]
    #
    i, j = len(arr), 1
    s = 0
    while j < len(arr):
        if arr[j] < pivot:
            s += arr[j]
            #
            if i != len(arr):
                temp = arr[j]
                arr[j] = arr[i]
                arr[i] = temp
                i += 1
        else:
            if i == len(arr):
                i = j
        #
        j += 1
    #
    temp = arr[i-1]
    arr[i-1] = arr[0]
    arr[0] = temp
    #
    return s, i-1
    
def balanced_split(arr):
    if len(arr) < 3:
        return False
    #
    s = sum(arr)
    #
    if s % 2 == 1:
        return False
    #
    h = s/2
    #
    while len(arr) > 0:
        lower_sum, k = quickSelect(arr)
        #
        if lower_sum == h:
            return True
        elif lower_sum < h:
            h -= lower_sum
            arr = arr[k:]
        else:
            arr = arr[:k]
    #
    return False

for test, ans in tests:
    print(balanced_split(test), ans)


### see: https://en.wikipedia.org/wiki/Quickselect#:~:text=In%20computer%20science%2C%20quickselect%20is,known%20as%20Hoare's%20selection%20algorithm

def partition(list, left, right, pivotIndex):
    pivotValue = list[pivotIndex]
    swap list[pivotIndex], list[right]  // Move pivot to end
    (list[pivotIndex],list[right]) = (list[right],list[pivotIndex])
    storeIndex = left
    for ix in range(left,right):
        if list[ix] < pivotValue:
            # swap list[storeIndex], list[ix]
            list[storeIndex], list[ix]
            list[ix], list[storeIndex]
            storeIndex += 1
    # swap list[right], list[storeIndex]  // Move pivot to its final place
    (list[right], list[storeIndex]) = (list[storeIndex], list[right])
    return storeIndex

# return k-th smallest element of list within left..right inclusive
# (i.e. left <= k <= right)
function select(list, left, right, k):
    # if list contains only one element, return that element
    if left = right:
        return list[left]
    # select a pivotIndex between left and right, e.g., left + floor(rand() % (right − left + 1))
    pivotIndex = partition(list, left, right, pivotIndex)
    # The pivot is in its final sorted position
    if k == pivotIndex:
        return list[k]
    elif k < pivotIndex:
        return select(list, left, pivotIndex − 1, k)
    else
        return select(list, pivotIndex + 1, right, k) 



