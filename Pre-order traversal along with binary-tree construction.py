class TreeNode:
   def __init__(self, val):
       self.data = val
       self.left = None
       self.right = None
      
def printPreorderTraversal(root):
   if root == None:
       return
   print(root.data, end = " ")
   printPreorderTraversal(root.left)
   printPreorderTraversal(root.right)
  
      
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


printPreorderTraversal(root)
