

class QueueUsingList:
    def __init__(self):
        self.queue = []
        self.front=0
        self.count=0

    def enque(self,data):
        self.queue.append(data)
        self.count=self.count+1

    def dequeue(self):
        if self.count==0:
            return -1
        element=self.queue[self.front]
        self.front=self.front+1
        self.count=self.count-1
        return element

    def size(self):
        return self.count

    def isEmpty(self):
        return self.count==0
    
    def front(self):
        if self.count==0:
            return -1
        return self.count[self.front]
