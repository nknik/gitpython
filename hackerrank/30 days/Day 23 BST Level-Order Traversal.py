#level order traversal 
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
        queue = [root]
        while len(queue) is not 0:
            c = queue[0]
            queue = queue[1:]
            print(str(c.data) + " ", end="")
            if c.left is not None:
                queue.append(c.left)
            if c.right is not None:
                queue.append(c.right)

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
