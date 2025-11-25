
class SLL:
    def __init__(self,head=None):
        self.head = head
        
        
class Node:
    def __init__(self, item=None,next=None):
        self.item = item
        self.next = next
        
        
n2 = Node(item=14,next=None)
n1 = Node(item=12,next=n2)
start = SLL(head=n1)

'''
[start | 200] -> [12 | 300] -> [14 | 400] -> [15 | None] 
      100           200           300           400
'''


listNode = list()
listNode.append({
    "node":"start",
    "addr":start.head
})
listNode.append({
    "node":"node",
    "addr":n1.next,
    "item":n1.item
})
listNode.append({
    "node":"node",
    "addr":n2.next,
    "item":n2.item
})

for i in listNode:
    print(i,end="\n")

