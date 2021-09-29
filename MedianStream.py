

'''
Given an input stream of N integers.
Your task is to insert these numbers into a new empty stream one by one
and after each insertion, print the median of all the integers read so far,
starting from the first integer till the last.

Input:
The first line of input contains an integer N denoting the number of elements in the stream.
Then the next N lines contain integer X denoting the number to be inserted into the stream.

Output:
For each element added to the stream print the floor of the new median in a new line.

Constraints:
1 <= N <= 10^6
1 <= x <= 10^6

Sample Input
4, 5, 15, 1, 3
Sample Output
5, 10, 5, 4
Time Limit: 1.5
Memory Limit: 256
Source Limit:
Explanation
Explanation

Flow in stream : 5, 15, 1, 3 
5 goes to stream --> median 5 (5) 
15 goes to stream --> median 10,  floor of(5+15)/2   =10 (5, 15) 
1 goes to stream --> median 5 (5,15,1) 
3 goes to stream --> median 4 ,  floor of(3+5)/2=8    (5, 15, 1, 3) 
'''


from heapq import heappush, heappop, heappushpop
class MedianFinder:
    def __init__(self):
        """ initialize your data structure here.
            create two heaps (L,R)
            each contains half data split at (current) median
            when single element, always on top of right heap
        """
        # L has data before median
        self.L_max_heap = []
        # R has data after median (may include median)
        self.R_min_heap = []
    #
    def addNum(self, num):
        """ push to R (min heap),
            then take min from right min heap, and push to left max heap
            comparison performed by push of pop
        """
        print("  add:",num)
        heappush(self.R_min_heap, num)
        heappush(self.L_max_heap, - heappop(self.R_min_heap))
        # adjust heap size,
        # since R heap may be smaller, move median to R heap
        if len(self.L_max_heap) > len(self.R_min_heap):
            heappush(self.R_min_heap, - heappop(self.L_max_heap))
        # print("  ",self.L_max_heap,self.R_min_heap)
    #
    # returns float
    def findMedian(self):
        """ when odd elements, return R heap
            when even elements, average L, R heap values
        """
        if len(self.R_min_heap) != len(self.L_max_heap):
            # print("  ",self.R_min_heap[0])
            return self.R_min_heap[0]
        else:
            # print("  ",self.R_min_heap[0],",", - self.L_max_heap[0])
            return (self.R_min_heap[0] - self.L_max_heap[0]) / 2

# def MedianStream(arr, n):
def medianFInd(arr, n):
    mobj = MedianFinder()
    for ix,x in enumerate(arr):
        mobj.addNum(x)
        print(ix,":",mobj.findMedian())
    return mobj.findMedian()

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

from bisect import bisect_left

# like insert sort, use bisect
class MedianFinderBisect:
    def __init__(self):
        """ initialize your data structure here.
        """
        self.oerdered = []
        return 
    #
    def addNum(self, num):
        """ bisect ordered list and insert at bisect point
        """
        insert_at = bisect_left(self.oerdered, num)
        self.oerdered.insert(insert_at, num)
        return 
    #
    def findMedian(self) -> float:
        """ whether length is even or odd, (left+right)/2 is median
        """
        # no matter the length is even or odd, (left+right)/2 is median
        left = self.oerdered[ len(self.oerdered) // 2 ]
        right = self.oerdered[ (len(self.oerdered)-1) // 2 ]
        return (left+right)/2

def medianFInd(arr, n):
    mobj = MedianFinderBisect()
    for ix,x in enumerate(arr):
        mobj.addNum(x)
        print(ix,":",mobj.findMedian())
    return mobj.findMedian()


def MeanStream(arr, n):
    n = len(arr)
    if n == 0: return 0
    if n == 1: return arr[0]
    mean = arr[0]
    for ix,x in enumerate(arr[1:):
        total += total + median
        count += 1
        if count % 2 == 0:
          median = floor(total/2)
        else:
          ...
    return mean
