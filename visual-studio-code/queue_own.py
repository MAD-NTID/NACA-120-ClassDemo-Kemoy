queue = []

"""
    return the number of elements in the queue
"""
def get_size():
    return len(queue)

"""
    Check if the queue is empty.
    Return True if the queue is empty. False if not empty
"""
def is_empty():
    #if get_size() == 0:
    #    return True
    #else:
    #    return False
    return get_size() == 0

def enqueue(element):
    queue.append(element)

def peek():
    front = queue[0]
    return front 

def dequeue():
    front = queue.pop(0)
    return front


#test
"""
print(get_size())
print(is_empty())
enqueue("Ragde")
enqueue("Justin")
enqueue("Brian")
print(get_size())
print(peek())
print(dequeue())
print(peek())

"""

