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

def printLL(head):
    curr = head
    while curr is not None:
        print(curr.data, end='->')
        curr = curr.next


def removeDuplicates(head):
    # Your code goes here
    if head == None:
        return head
    t1 = head
    t2 = head
    while t2:
        if t1.data == t2.data:
            t2 = t2.next
        elif t1.data != t2.data:
            t1.next = t2
            t1 = t2
            t2 = t2.next
    return head

def printReverse(head) :
    #Your code goes here
    if head==None :
        return
    printReverse(head.next)
    print(head.data,end=" ")
    return
a=[1,2,3,3,3,4,4,4,4,5,5,6,6,7]
a1=[1,2,3]
head=listToLLwithHead(a1)
printReverse(head)

