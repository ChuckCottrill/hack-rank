

Diameter of Binary Tree

'''
Welcome to Facebook!

This is just a simple shared plaintext pad, with no execution capabilities.

When you know what language you would like to use for your interview,
simply choose it from the dropdown in the top bar.

Enjoy your interview!

#1: diameter pass through root

            2
           / \
          7   3
         / \   \
        6   9   1
           / \   \
          11  4   5

#2: diameter does not pass through root

          0
           \
            2
           / \
          7   3
         / \   \
        6   9   1
           / \   \
          11  4   5

# Node = { data`, left, right }
'''

# Python3 program to find the diameter of binary tree
 
# A binary tree node
class Node:
    # Constructor, to create Node
    def __init__(self, data, left = None, right = None ):
        self.data = data
        self.left = left # None
        self.right = right # None
    #
    def addL(self, node, data):
        newnode = Node(data)
        node.left = newnode
    #
    def addR(self, node, data):
        newnode = Node(data)
        node.right = newnode

class Height:
    # constructor, create Height
    def __init__(self, height=0):
        self.h = height
    #
    def add(self, val):
        node.h += val

# Compute the "height" of a tree
# height of binary tree
# height is number of nodes along longest path from node to leaf node
def height(node):
    # base: subtree is empty
    if node is None:
        return 0
    # when tree not empty, height = 1 + max( height(left), height(right) )
    lheight = height(node.left)
    lheight = height(node.right)
    return 1 + max(height(node.left), height(node.right))

# diameter of binary tree
def diameter(node):
    # base: subtree is empty
    if node is None:
        return 0
    # height of left, right subtree
    lheight = height(node.left)
    rheight = height(node.right)
    # diameter of left, right subtree
    ldiameter = diameter(node.left)
    rdiameter = diameter(node.right)
    # diameter of subtree at node
    # a) diameter of left subtree
    # b) diameter of right subtree
    # c) height of left subtree + height of right subtree + 1
    return max(lheight + rheight + 1, max(ldiameter, rdiameter))

# diameter of binary tree, with height
def diameterH(node,height):
    # base: subtree is empty
    if node is None:
        height.h = 0
        return 0
    # height of left, right subtree
    lheight = Height(0)
    rheight = Height(0)
    # diameter of left, right subtree
    ldiameter = diameterH(node.left,lheight)
    rdiameter = diameterH(node.right,rheight)
    # height of subtree = max of height of left, right subtree + 1
    height.h = max(lheight.h, rheight.h) + 1
    # diameter of subtree at node
    # a) diameter of left subtree
    # b) diameter of right subtree
    # c) height of left subtree + height of right subtree + 1
    return max(lheight.h + rheight.h + 1, max(ldiameter, rdiameter))

def diameter(node):
    height = Height(0)
    return diameterH(node,height)

# Driver Code
'''
            2
           / \
          7   3
         / \   \
        6   9   1
           / \   \
          11  4   5
'''
tree1 = Node(2,
    Node(7, Node(6), Node(9, Node(11), Node(4) ) ),
    Node(3, None, Node(1, None, Node(5) ) )
    )
print(diameter(tree1))

'''
#2: diameter does not pass through root

          17
           \
            2
           / \
          7   3
         / \   \
        6   9   1
           / \   \
          11  4   5
'''

tree2 = Node(17, None,
    Node(2,
    Node(7, Node(6), Node(9, Node(11), Node(4) ) ),
    Node(3, None, Node(1, None, Node(5) ) )
    ) )
print(diameter(tree2))

'''
Example constructed binary tree
            1
          /   \
        2      3
      /  \
    4     5
'''

n4 = Node(4)
n5 = Node(5)
# n2 = Node(2, Node(4), Node(5) )
n2 = Node(2, n4, n5 )
n3 = Node(3)
tree3 = Node(1, n2, n3 )
# root.left.left = Node(4)
# root.left.right = Node(5)

tree3 = Node(1,
    Node(2, Node(5), Node(5) ),
    Node(3, None, None)
    )
 
# Function Call
print(diameter(tree3))


