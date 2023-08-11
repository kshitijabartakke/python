# Linked List
# Element of linked list called as node
# Node stores 1) data 2) address of next element
# One element(node) of Linked list stores memory address/info of its next element
# First Item of the Linked List called as Head

class Node:
    def __init__(self,data):
        self.data = data
        self.nextval = None

class LinkedList:
    def __init__(self):
        self.head =  None  #Defyining that head is None; means your linked list is empty

    def traverse(self):
        current = self.head

        while current is not None:
            print(current.data)
            current = current.nextval
    
if __name__ == "__main__":
    n1 = Node(100)
    n2 = Node(200)
    n3 = Node(300)
    #print(n1.data)

    linked_list = LinkedList()
    linked_list.head = n1
    linked_list.head.nextval = n2
    n2.nextval = n3
    n3.nextval = None


    linked_list.traverse()


