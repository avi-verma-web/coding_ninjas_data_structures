import queue


def reverseQueue(queue) :
    if queue.empty():
        return
    item = queue.get()
    
    reverseQueue(queue)
    queue.put(item)