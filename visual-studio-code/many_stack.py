def create_stack():
    return []

def push(stack,element):
    stack.insert(0, element)

def size(stack):
    return len(stack)

def pop(stack):
    return stack.pop(0)

def top(stack):
    return stack[0]

def is_empty(stack):
    return size(stack) == 0


""""
example_stack_1 = create_stack()
push(example_stack_1, "trent")

example_stack_2 = create_stack()
push(example_stack_2, "Ragde")

size_1 = size(example_stack_1)
size_2 = size(example_stack_2)
print(f"Stack 1 size: {size_1} and Stack 2 size: {size_2}")
"""