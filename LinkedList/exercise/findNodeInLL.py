def findNode(head, n) :
    # Write your code here.
    curr=head
    index=0
    while curr:
        if curr.data==n:
            return index
        index=index+1
        curr=curr.next
    return -1