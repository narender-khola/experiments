class Queue:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def enque(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)
    
    def printQueue(self):
        print(self.items)

s = Queue()
s.enque(1)
s.enque(2)
s.enque(3)
s.printQueue()
s.dequeue()
s.printQueue()
