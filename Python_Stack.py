# Stack
# LIFO -  Last in First Out
# Insert-Push  - Remove-Pop
import array
class Stack:
    def __init__(self):
        self.my_stack = array.array('i',[])

    def is_empty(self):
        if len(self.my_stack):
            return False
        else:
            return True
        
    def push(self,element):
        self.my_stack.append(element)

    def pop(self):
        if self.is_empty():
            print("Stack is Empty Can't pop")
        else:
            self.my_stack.pop()
if __name__ ==  "__main__": # This is default python syntax; tells you that it will run first when we execute the code
    stack = Stack()        #Create Object in Python

    stack.push(100)
    print(stack.my_stack)  #Output array('i', [100])
    stack.push(200)
    stack.push(300)
    print(stack.my_stack)  #Output array('i', [100, 200, 300])


    stack.pop()
    print(stack.my_stack)  #Output array('i', [100, 200]) ; last element got removed
    stack.pop()
    print(stack.my_stack)  #Output array('i', [100]) ; last element got removed
