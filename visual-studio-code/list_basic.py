
todos = ["Wash car", "Cook", "Clean bathroom"]
print(todos)
print(len(todos))

""""
for item in todos:
    print(item)
"""
print(todos[0])
#print(todos[3]) will crash

todos.append("Sleep")
print(todos[3]) 
print(todos)
todos[3] = "New name"
print(todos)
print(len(todos))

todos.insert(2, "Watch movie")
print(todos)

todos.remove("Watch movie")
print(todos)