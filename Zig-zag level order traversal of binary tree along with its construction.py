class TreeNode:
   def __init__(self, val):
       self.data = val
       self.left = None
       self.right = None
      
def printZigZagLevelorderTraversal(root):
   if root == None:
       return
   result = []
   Q = []
   Q.append(root)
   level = 0
  
   while Q:
       n = len(Q)
       currLevel = []
       for i in range(n):
           curr = Q.pop(0)
           currLevel.append(curr.data)
           if curr.left != None:
               Q.append(curr.left)
              
           if curr.right != None:
               Q.append(curr.right)
              
       if level % 2 != 0:
           currLevel = currLevel[::-1]
       result.append(currLevel)
       level += 1
  
   for eachOne in result:
       for ele in eachOne:
           print(ele, end = " ")
       print()
  
      
root = TreeNode(11)
root.left = TreeNode(7)
root.right = TreeNode(15)
root.left.left = TreeNode(5)
root.left.right = TreeNode(9)
root.left.left.left = TreeNode(3)
root.left.right.left = TreeNode(8)
root.left.right.right = TreeNode(10)
root.right.left = TreeNode(13)
root.right.right = TreeNode(20)
root.right.left.left = TreeNode(12)
root.right.left.right = TreeNode(14)
root.right.right.left = TreeNode(18)
root.right.right.right = TreeNode(25)


printZigZagLevelorderTraversal(root)
