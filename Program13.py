class Stack:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        if len(self.items)==0:
            return True
        else:
            return False
    
    def push(self,data):
        self.items.append(data)
    
    def pop(self):
        if not self.isEmpty():
            self.items.pop()
        else:
            print("Popping is not possible since the stack does not contain any elements")
    
    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            print("No items are present in the stack")

class Queue:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        if len(self.items)==0:
            return True
        else:
            return False
    
    def enqueue(self,data):
        self.items.append(data)
    
    def dequeue(self):
        if not self.isEmpty():
            self.items.pop(0)
        else:
            print("Dequeuing is not possible since the queue does not contain any elements")
    
    def peek(self):
        if not self.isEmpty():
            return self.items[0]
        else:
            print("No items are present in the Queue")


stack = Stack()
print(f"Is the stack empty now?{stack.isEmpty()}")
stack.push(2)
stack.push(5)
stack.push(3)
stack.push(4)
print(f"The top most part of the stack is {stack.peek()}")
stack.pop()
stack.pop()
stack.pop()
stack.pop()
print(f"Is the stack empty now?{stack.isEmpty()}")
queue = Queue()
print(f"Is the queue empty now?{queue.isEmpty()}")
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
print(f"The top most part of the queue is {queue.peek()}")
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
print(f"Is the queue empty now?{queue.isEmpty()}")
