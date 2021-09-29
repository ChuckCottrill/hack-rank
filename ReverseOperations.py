
# Reverse Operations

'''
Reverse Operations

You are given a singly-linked list that contains N integers.
A subpart of the list is a contiguous set of even elements, bordered either by the end of the list or an odd element.
For example, if the list is [1, 2, 8, 9, 12, 16], the subparts of the list are [2, 8] and [12, 16].
Then, for each subpart, the order of the elements is reversed.
In the example, this would result in the new list, [1, 8, 2, 9, 16, 12].
The goal of this question is: given a resulting list, determine the original order of the elements.
Implementation detail:
You must use the following definition for elements in the linked list:

class Node {
    int data;
    Node next;
}
Signature
Node reverse(Node head)
Constraints
1 <= N <= 1000, where N is the size of the list
1 <= Li <= 10^9, where Li is the ith element of the list
Example
Input:
N = 6
list = [1, 2, 8, 9, 12, 16]
Output:
[1, 8, 2, 9, 16, 12]
'''

### see: https://www.tutorialspoint.com/python_data_structure/python_linked_lists.htm

class Node:
    def __init__(self, data=None):
        self.data = data
        self.link = None
    #
    def toarr(self):
        arr = []
        arr.append(self.data)
        node = self.link
        while node is not None:
            arr.append(node.data)
            node = node.link
        return arr
    #
    def listprint(self):
        print(self.data)
        arr = self.toarr()
        print(",".join([str(x) for x in arr]))

class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    #
    def add(self,val):
        node = Node(val)
        if self.head == None:
            self.head = node
        if self.tail != None:
            self.tail.link = node
        self.tail = node
    #
    def toarr(self):
        arr = []
        node = self.head
        while node is not None:
            arr.append(node.data)
            node = node.link
        return arr
    #
    def listprint(self):
        arr = self.toarr()
        print(",".join([str(x) for x in arr]))

# return Node
def reverse(head):
    # Write your code here
    """ head Node
        return Node
    """
    node = head
    evens = []
    while node is not None:
        isEven = node.data % 2 == 0
        # push node to evens
        if isEven:
            # print("  push:",node.data)
            evens.append(node)
        # not even, reverse nodes in evens
        if not isEven or node.link is None:
            # print("  len(evens):", len(evens))
            while len(evens) > 1:
                # swap data for matched pair in evens
                # print("  swap:",evens[0].data,evens[-1].data)
                evens[0].data, evens[-1].data = evens[-1].data, evens[0].data
                evens.pop(0)
                evens.pop(-1)
            evens.clear()
        node = node.link
    return head

def reverseOperations(arr):
    slist = SLinkedList()
    for x in arr:
        slist.add(x)
    slist.listprint()
    head = reverse(slist.head)
    # head.listprint()
    p = head.toarr()
    print(p)
    slist.listprint()
    # p = slist.toarr()
    # print(p)

reverseOperations([1,2,4,6,8,7,3,4,2,5,9,4,8,2])
reverseOperations([1,2,4,6,8,7,3,4,2,5,9,2,4,6,7,13,4,8,2])


#####

# General linked list reversal function
def reverseLL(head):
    prev = None
    node = head
    while node and node.data % 2 == 0:
        temp = node.next
        node.link = prev
        prev = node
        node = temp
    if not node:
        # if the while loop invariant broke due node being None
        nextPart = None
    else:
        # if the while loop invariant broke due node data being odd
        nextPart = node
    return (prev, nextPart)

def reverse(head):
    # Write your code here
    node = head
    prev = dummy = Node("dummy")
    dummy.link = head
    ans = []
    while node:
        # odd = node.data % 2
        if node.data % 2:
            # node data value is odd
            prev = node
            node = node.link
        # even
        else:
            # reverse linked list and get newHead for the reversed list + node for the start of next part
            newHead, nextPart = reverseLL(node)
            prev.link = newHead
            node.link = nextPart
            node = node.next
    return dummy.next




