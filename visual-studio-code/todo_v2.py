todos = []
menu = ["Add task", "View tasks","Remove task", "Update task","Quit"]


"""
    This function shows the menu for the todos
"""
def show_menu():
    print("Menu\n==============")
    for i in range(len(menu)):
        print(str(i+1) + "." + menu[i])

def selection(max):
    while True:
        try:
            choice = int(input("Choice:"))
            if choice < 1 or choice > max:
                raise ArithmeticError("Pick between 1 and " + str(max))
            return choice
        except ValueError as e:
            print("Please enter number only!")
        except ArithmeticError as e:
            print(e)

def add_to_list():
    while True:
        task = input("Enter the task:")
        if task.isdigit() or task=="":
            print("Task cannot be empty or digit!")
            continue
        else:
            break
    #task format <taskname>,<task status>
    todos.append(task+",todo")
    print(task +" was added to the list")

def view_tasks():
    if len(todos) == 0:
        print("No tasks to display")
    else:
        print("Tasks:\n=======")
        i = 1
        for task in todos:
            print(str(i)+"."+task)
            i+=1

def get_task_number(prompt):
    while True:
        view_tasks()
        task = int(input(prompt+":"))
        if task < 1 or task > len(todos):
            raise ArithmeticError("Enter a number between 1-" + str(len(todos)))
        return task
    
def remove_task():
    while True:
        try:
            view_tasks()
            task = int(input("Enter the number of the task to remove:"))
            if task < 1 or task > len(todos):
                raise ArithmeticError("Enter a number between 1-" + str(len(todos)))
            deleted = todos.pop(task-1)
            print("Task:" + deleted + " successfully removed")
            break
        except ValueError as e:
            print(e)
            print("Enter digits only!!!")
        except ArithmeticError as e:
            print(e)
def update_task():
    while True:
        view_tasks()
        try:
            task = int(input("Enter the task:"))
            if task < 1 or task > len(todos):
                raise ArithmeticError("Enter a number between 1-" + str(len(todos)))
            pick = 0
            while True:
                print("What do you want to do?")
                print("1. update task name\n2. update task status")
                pick = int(input("choice:"))
                old_task = todos[task-1]
                old = old_task.split(",")
                if pick == 1:
                    while True:
                        new_task = input("Enter the new name for the task:")
                        if new_task.isdigit() or new_task=="":
                            print("The task name cannot be empty")
                            continue
                        new_task = new_task + "," + old[1]

                        break
                else:
                    status = input("Enter the status:")
                    new_task = old[0] + "," + status
                        
                todos[task-1] = new_task
                print("The task was successfully updated")
                break
            break
        except ValueError:
            print("Digits only!")
        except ArithmeticError as e:
            print(e)
def main():
    while True:
        show_menu()
        choice = selection(len(menu))
        if choice == 1:
            add_to_list()
        elif choice == 2:
            view_tasks()
        elif choice == 3:
            remove_task()
        elif choice == 4:
            update_task()
        else:
            print("Thank you for using the NACA-120 - 01 TODOS!!!")
            print("Bye....for now....hahaha......")
            break
        
        print("\n")

main()