
class StackUsingArray:

    def __init__(self):
        self.data = []

    def push(self, ele):
        self.data.append(ele)

    def pop(self):
        return "Stack is Empty" if len(self.data) == 0 else self.data.pop()

    def top(self):
        return "Stack is Empty" if len(self.data) == 0 else self.data[-1]

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return True if len(self.data) == 0 else False


a = StackUsingArray()

print(a.top())
print(a.isEmpty())
