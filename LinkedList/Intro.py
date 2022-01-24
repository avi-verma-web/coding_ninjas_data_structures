from ast import Not


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def listToLLwithHead(a):
    head = None
    for currData in a:
        # creating new node
        newNode = Node(currData)
        if head is None:
            head = newNode
        else:
            # Linking new node to linked List
            curr = head
            while curr.next is not None:
                curr = curr.next
            curr.next = newNode
    return head


def listToLLwithHeadAndTail(a):
    head = None
    tail = None
    for ele in a:
        newNode = Node(ele)
        if head == None and tail == None:
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = newNode
    return head


def printLL(head):
    curr = head
    while curr is not None:
        print(curr.data, end='->')
        curr = curr.next


def getLength(head):
    count = 0
    while head is not None:
        count = count+1
        head = head.next
    return count


def getIth(head, i):
    count = 0
    curr = head
    while curr:
        if count == i:
            return curr.data
        count = count+1
        curr = curr.next


def insertAtIth(head, i, data):
    if i < 0 or i > getLength(head):
        return head
    count = 0
    curr = head
    prev = None
    while count < i:
        count = count+1
        prev = curr
        curr = curr.next
    newNode = Node(data)
    if prev is not None:
        prev.next = newNode
        newNode.next = curr
    else:
        # insert at first position
        newNode.next = head
        head = newNode
    return head


def deleteAtIth(head, i):
    if i < 0 or i >= getLength(head):
        return head
    curr = head
    prev = None
    count = 0
    while count != i:
        count = count+1
        prev = curr
        curr = curr.next
    # first node
    if prev is None:
        head = curr.next
    # last node
    elif curr.next is None:
        prev.next = None
    elif curr.next is not None:
        prev.next = curr.next
    return head


def getLengthRecursive(head):
    if head is None:
        return 0
    elif head.next is None:
        return 1
    return 1+getLengthRecursive(head.next)


arr = [1, 3, 4, 5, 6]

head = listToLLwithHeadAndTail(arr)
print(getLengthRecursive(head))
