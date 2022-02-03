class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

class QueueUsingLL :
    def __init__(self):
        self.head = None
        self.tail = None
        self.count=0

    def getSize(self) :
        return self.count

    def isEmpty(self) :
        return self.head==None

    def enqueue(self, data) :
        newNode = Node(data)
        if self.head == None and self.tail == None:
            self.head = newNode
            self.tail = newNode
        elif self.tail!=None:
            self.tail.next = newNode
            self.tail = newNode
        self.count=self.count+1

    def dequeue(self) :
        if self.head == None:
            return -1
        else:
            element = self.head.data
            if self.head.next == None:
                self.head = None
                self.tail=None
            else:
                self.head = self.head.next
            self.count=self.count-1
            return element

    def front(self) :
        if self.head == None:
            return -1
        return self.head.data

        



