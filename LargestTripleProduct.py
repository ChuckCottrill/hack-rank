



import math
from queue import PriorityQueue

def LargestTripletMultiplicationSimple(arr, n):
    """ sort array, then extract last n
    """
    product = -1
    if len(arr) < 3: return product
    numbers = arr[:]
    numbers.sort()
    # keep = numbers[-n:]
    x = numbers[-3]
    y = numbers[-2]
    z = numbers[-1]
    # (x,y,z) = (numbers[-3], numbers[-2], numbers[-1])
    product = x * y * z
    return product

from heapq import heapify, heappush, heappushpop, nlargest
class MaxHeap():
    def __init__(self, maxsize):
        self.h = []
        self.length = maxsize
        heapify( self.h )
    #
    def add(self, element):
        if len(self.h) < self.length:
            heappush(self.h, element)
        else:
            heappushpop(self.h, element)
    #
    def size(self):
        return len(self.h)
    #
    def getTop(self):
        return sorted(self.h, reverse=True)

# Print product of three largest numbers in subarray arr[0..ix]
def LargestTripletMultiplicationHeap(arr, n):
    """ use MaxHeap(3)
    """
    product = -1
    if len(arr) < 3: return -1
    # create maxHeap (3)
    q = MaxHeap(3)
    # scan array, find (3) largest numbers
    # for ix in range(n):
    for ix in range(len(arr)):
        # push arr[ix] to MaxHeap(3)
        q.add(arr[ix])
        top = q.getTop()
        if len(top) >= 3:
            # three largest elements from priority queue
            x = top[0]
            y = top[1]
            z = top[2]
            # (x, y, z) = (top[0], top[1], top[2])
            # product
            product = (x * y * z)
            # print("[",ix,"]:",product)
    # when less than three elements, result is = -1
    top = q.getTop()
    # print(top)
    # if len(top) < 3: return -1
    print(product)
    return product

# Print product of three largest numbers in subarray arr[0..ix]
def LargestTripletMultiplication(arr, n):
    """
    """
    product = -1
    if len(arr) < 3: return product
    # create priority queue
    q = PriorityQueue()
    # scan array, find largest numbers
    for ix in range(n):
        # push -arr[ix] to get max PriorityQueue
        q.put(-arr[ix])
        if (q.qsize() >= 3):
            # pop three largest elements from priority queue
            x = q.get()
            y = q.get()
            z = q.get()
            # replace three largest to priority queue
            q.put(x);
            q.put(y);
            q.put(z);
            # product
            product = -(x * y * z)
        # If less than three elements
        # are present in array print -1
    if (q.qsize() < 3):
            product = -1
    print(-product)
    return -product

# Driver Code
if __name__ == '__main__':
  
    arr = [ 1, 2, 3, 4, 5 ]
    n = len(arr)
     
    LargestTripletMultiplication(arr, n)
     
