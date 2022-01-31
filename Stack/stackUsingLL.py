class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class StackUsingLL:
    def __init__(self):
        self.head = None
        self.count = 0

    def push(self, ele):
        newNode = Node(ele)
        newNode.next=self.head
        self.head = newNode
        self.count = self.count+1

    def pop(self):
        if self.count == 0:
            return "Stack is Empty"
        temp = self.head.data
        self.head = self.head.next
        self.count = self.count-1
        return temp

    def top(self):
        if self.count == 0:
            return "Stack is Empty"
        return self.head.data

    def size(self):
        return self.count

    def isEmpty(self):
        return True if self.count == 0 else False

a = StackUsingLL()

a.push(2)
a.push(3)
print(a.top())
print(a.isEmpty())