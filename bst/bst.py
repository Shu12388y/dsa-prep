from node import Node

class BST:
    def __init__(self):
        self.root = None
        
        
    def insert(self,root,key:int):
        if root is None:
            return Node(key)
        
        if key < root.key:
            root.left = self.insert(root.left,key)
            
        else:
            root.right = self.insert(root.right,key)
            
        return Node
            
    
    def transversal(self,root):
        if root:
            self.transversal(root.left)
            print(root.key,end=" ")
            self.transversal(root.right)

             
