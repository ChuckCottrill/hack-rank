

### Number of Visible Nodes
### see: L


### see: https://www.geeksforgeeks.org/count-the-number-of-visible-nodes-in-binary-tree/
### see: https://codesays.com/2014/solution-to-count-visible-nodes-in-binary-tree/

'''
'''



# Number Visible Nodes
def NumberVisibleNodes(arr):
    pass

# count the number of visible nodes in binary tree
 
import sys

# Node contains data value and left, right child
class newNode:
    def __init__(self, data):
        """ constructor allocates new node with given data, and left, right child pointers
        """
        self.data = data
        self.left = None
        self.right = None

# Variable to keep the track of visible nodes
# countNode = 0
# global countNode
 
# perform the preorder traversal for binary tree
def preOrder(node, mx):
    """ visit node,
        process left subtree
        process right subtree
        return results
    """
    count = 0
    # node empty
    if (node == None):
        return mx, 0
    # If the current node value
    # is greater or equal to the
    # max value, then update count
    # variable and also update max
    # variable
    if (node.data >= mx):
        count += 1
        mx = max(node.data, mx)
    # descend left subtree
    (lmx,lcount) = preOrder(node.left, mx)
    # descend right subtree
    (rmx,rcount) = preOrder(node.right, mx)
    # if lmx > mx: mx = lmx
    # if rmx > mx: mx = rmx
    return mx, count+lcount+rcount

def run():
    """
            5
           /  \
         3     10
        /  /   /
       20   21 1
    """
    root = newNode(5)
    root.left = newNode(3)
    root.right = newNode(10)
    root.left.left = newNode(20)
    root.left.right = newNode(21)
    root.right.left = newNode(1)
    (mx,countNode) = preOrder(root, -sys.maxsize-1)
    print(countNode)

# Driver code
if __name__ == '__main__':
   
     


