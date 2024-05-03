class TreeNode:
  def __init__(self, val):
      self.data = val
      self.left = None
      self.right = None
def collectLeftView(root, result):
   if root == None or (root.left == None and root.right == None):
       return
  
   result.append(root.data)
   if root.left != None:
       collectLeftView(root.left, result)
   else:
       collectLeftView(root.right, result)
      
def collectLeaves(root, result):
   if root == None:
       return
  
   if root.left == None and root.right == None:
       result.append(root.data)
       return
  
   collectLeaves(root.left, result)
   collectLeaves(root.right, result)
      
      
def collectRightView(root, result):
   temp = []
   curr = root
   while curr != None:
       if curr.left == None and curr.right == None:
           break
       temp.append(curr.data)
       if curr.right != None:
           curr = curr.right
       else:
           curr = curr.left
          
   temp = temp[::-1]
   for ele in temp:
       result.append(ele)
  
  
def boundaryTraversal(root):
   if root == None:
       return
  
   result = []
   result.append(root.data)
   collectLeftView(root.left, result)
   collectLeaves(root, result)
   collectRightView(root.right, result)
    for ele in result:
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




boundaryTraversal(root)
