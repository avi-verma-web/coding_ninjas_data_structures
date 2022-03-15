import queue
queue.Queue().qsize()
def reverseQueue(queue) :
    if queue.empty():
        return
    item = queue.get()
    
    reverseQueue(queue)
    queue.put(item)