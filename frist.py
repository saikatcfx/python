# print("hello world")
class node:
    def __init__(self,data):
        self.data=data
        self.next=None

node1=node(10)
node2=node(20)
node3=node(30)

node1.next=node2
node2.next=node3

current_node=node1

while current_node is not None:
    print(current_node.data,end="->")
    current_node=current_node.next

