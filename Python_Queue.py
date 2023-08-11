# Queue
# FIFO - First In First Out
# Insert-Enqueue , Remove-dequque
# Creating a Queue using array
import array
class Queue:
    def __init__(self):
        self.my_quque = array.array('i',[])
    
    def is_empty(self):
        if len(self.my_quque):
            return False
        else:
            return True
        
    def enqueue(self,element):
        self.my_quque.append(element)

    def deuquue(self):
        if self.is_empty():
            print("Queue is Empty Can't Dequque")
        else:        
            self.my_quque.pop(0)   # Remove first index of the queue using FIFO method

if __name__ == "__main__":
    queue = Queue()
    print(queue.my_quque)  #Output array('i') # Empty Queue

    queue.enqueue(100)
    print(queue.my_quque)  #Output array('i', [100])
    queue.enqueue(300)
    queue.enqueue(600)
    print(queue.my_quque)  #Output array('i', [100, 300, 600])

    queue.deuquue()
    print(queue.my_quque)  #Output array('i', [300, 600])
    queue.deuquue()
    print(queue.my_quque)  #Output array('i', [600])
    queue.deuquue()
    print(queue.my_quque)  #Output array('i')

    

