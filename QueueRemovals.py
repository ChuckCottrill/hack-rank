


### Queue Removals
### see:

'''
Given given a list of n integers arr, which represent elements in a queue (in order from front to back).
Also given an integer x,
perform x iterations of the following 3-step process:
    Pop x elements from the front of queue (or, if it contains fewer than x elements, pop all of them)
    find the element with the largest value from elements that were popped, and remove that element
        (if there are multiple such elements, take the one which had been popped the earliest)
    For each one of the remaining elements that were popped (in the order they had been popped),
        decrement its value by 1 if value is positive (otherwise, if its value is 0, then value left unchanged),
    and then add it back to the queue
Compute a list of x integers output,
the ith of which is the 1-based index in the original array of the element which had been removed in step 2 during the ith iteration

Signature
int[] findPositions(int[] arr, int x)
Input
x is in the range [1, 316].
n is in the range [x, x*x].
Each value arr[i] is in the range [1, x].

Output
Return a list of x integers output, as described above.
Example
n = 6
arr = [1, 2, 2, 3, 4, 5]
x = 5
output = [5, 6, 4, 1, 2]
The initial queue is [1, 2, 2, 3, 4, 5] (from front to back).
Explaination

In the first iteration, the first 5 elements are popped off the queue, leaving just [5]. Of the popped elements, the largest one is the 4, which was at index 5 in the original array. The remaining elements are then decremented and added back onto the queue, whose contents are then [5, 0, 1, 1, 2].
In the second iteration, all 5 elements are popped off the queue. The largest one is the 5, which was at index 6 in the original array. The remaining elements are then decremented (aside from the 0) and added back onto the queue, whose contents are then [0, 0, 0, 1].
In the third iteration, all 4 elements are popped off the queue. The largest one is the 1, which had the initial value of 3 at index 4 in the original array. The remaining elements are added back onto the queue, whose contents are then [0, 0, 0].
In the fourth iteration, all 3 elements are popped off the queue. Since they all have an equal value, we remove the one that was popped first, which had the initial value of 1 at index 1 in the original array. The remaining elements are added back onto the queue, whose contents are then [0, 0].
In the final iteration, both elements are popped off the queue. We remove the one that was popped first, which had the initial value of 2 at index 2 in the original array.
'''

class Solution:
    def findLargest(self,ray):
        """ find largest value in array
            return index of first value matching largest value
        """
        # largest value?
        best = max(ray)
        # find position of max element?
        ix = ray.index(best)
        # print("ix:",ix,",max:",best)
        return ix, best
    #
    def decrementPositive(self,x):
        return x-1 if x > 0 else x
    #
    def process(self,queue,x):
        """ step
            Pop x elements from the front of queue (or, if it contains fewer than x elements, pop all of them)
            find element with largest value from elements popped, and remove it
                (if there are multiple such elements, take the element which was popped the earliest)
            For each one of the remaining elements that were popped (in the order they had been popped),
                decrement element value by 1 if element positive (otherwise, if value is 0, then value left unchanged)
            and then add it back to the queue
        """
        n = len(queue)
        if x > n: x = n
        # front = []
        # for ix in range(x):
        #     front.append(queue.pop[0])
        front = queue[0:x]
        queue = queue[x:]
        # print("front:",front)
        # find largest and remove
        (pos,best) = self.findLargest(front) # len(front)
        # del front[pos]
        front.pop(pos)
        front = [ self.decrementPositive(x) for x in front ]
        # front = [ x-1 if x > 0 else x for x in front ]
        # print("front:",front)
        for x in front:
            queue.append(x)
        return queue
    #
    def findPositions(self, arr, x):
        """ findPositions
            int[] arr
            int x)
            return int[]
        """
        print("queue:",arr)
        for ix in range(x):
            arr = self.process(arr,x)
            print("queue:",arr)
        return arr

obj = Solution()
obj.findPositions( [1,2,4,6,8,7,3,4,2,5,9,4,8,2], 5 )
obj.findPositions( [1,2,4,6,8,7,3,4,2,5,9,2,4,6,7,13,4,8,2], 7 )




