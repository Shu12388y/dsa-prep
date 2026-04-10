# class Node:
#     def __init__(self,key):
#         self.key = key
#         self.right = None
#         self.left = None 
        
        
# class BST:
#     def __init__(self):
#         self.root = None
        
#     def insert(self,root,key):
#         if root is None:
#             return Node(key)
        
#         if key < root.key:
#             root.left = self.insert(root.left, key)
#         else:
#             root.right = self.insert(root.right,key)
        
#         return root
    
#     def tranveral(self,root):
#          if root:
#              self.tranveral(root.left)
#              print(root.key,end=" ")
#              self.tranveral(root.right)
        
    
# bst = BST()
# bst.root = bst.insert(bst.root,12)
# bst.insert(bst.root, 5)
# bst.insert(bst.root, 15)

# bst.tranveral(bst.root)


from bst import BST

b = BST()
b.root = b.insert(b.root,10)
b.insert(b.root,11)
b.insert(b.root,13)


b.transversal(b.root)
