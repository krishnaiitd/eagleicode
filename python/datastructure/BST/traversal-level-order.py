import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root


def levelOrder(self,root):
    
    #Write your code here
    #llist = []
    #alist = [root]
    #while len(alist) > 0:
    #    llist = llist + [l.data for l in alist]
    #    print('left node', [l.left.data for l in alist if l.left])
    #    print('right node', [l.right.data for l in alist if l.right])
    #    print([l.data for l in alist])
    #    alist = [l.left for l in alist if l.left] + [l.right for l in alist if l.right]
    #
    #print(' ' . join(map(str, llist)))
    
    # In order traversal for testing 
    queue =  [root] if root else []
    while queue:
        node = queue.pop()
        print(node.data, end=" ")
        
        if node.left: queue.insert(0, node.left)
        
        if node.right: queue.insert(0, node.right)


T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)        