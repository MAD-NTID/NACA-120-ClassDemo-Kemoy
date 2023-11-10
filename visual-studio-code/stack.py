stack = []

"""
    This returns the number of elements on the stack
"""
def get_size():
    return len(stack)

"""
    This check if the stack is empty.
    return true if empty and false otherwise
"""
def is_empty():
    if get_size() == 0:
        return True
    else:
        return False
"""
    This will add an element to the "top" of the stack by putting it at the front
"""
def push(element):
    stack.insert(0, element)

"""
    This will remove and return the top element
"""
def pop():
    top = stack.pop(0)
    return top

def get_top():
    top = stack[0]
    return top




""""
print("Stack size:", get_size())
print("Stack is empty? ", is_empty())
push("Justin")
push("Trent")
print("Stack size:", get_size())
print("The top element is:", get_top())
print("Removing element from the top: ", pop())
print("The top element is:", get_top())
"""

