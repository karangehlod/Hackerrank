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
        #queue for this search 
        que=[]
        ans=''
        que.append(root)
        while(len(que)>0):
            x= que.pop(0)
            if x.left!= None :
                que.append(x.left)
            if x.right != None:
                que.append(x.right)
            ans += str(x.data) +" "
            #self.levelOrder(x)
        print(ans)
        #return ans

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
