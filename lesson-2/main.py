
class SLL:
    def __init__(self,head=None):
        self.head = head


class Node:
    def __init__(self, item=None,next=None):
        self.item = item
        self.next = next
        
        
'''
[start | 200] -> [12 | 300] -> [14 | 400] -> [15 | None] 
      100           200           300           400
'''




# n2 = Node(item=13,next=None)
# n1 = Node(item=12,next=n2)
# head = SLL(head=n1)



N = int(input("Enter the number of node: "))
i = 0
ref_node = None 
while i <= N:
    item = int(input("Enter value: "))
    if ref_node == None:
        n = Node(item=item,next=None) 
        ref_node = n
        head = SLL(head=n)
        print(ref_node,head,end="\n")
        i = i +1
    else:
        n = Node(item=item,next=ref_node)
        ref_node = n
        print(ref_node,end="\n")
        i =  i+1