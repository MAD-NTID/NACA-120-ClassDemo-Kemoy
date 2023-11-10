from many_stack import *

menus = [
    "Buy a new pringle can",
    "Eat a pringle chip",
    "Exit"
]

#keep a list of all pringle cans we have
#cans = []
cans = {}

def select_menu():
    i = 1
    for menu in menus:
        print(f"{i}. {menu}")
        i+=1

    choice = input("Selection:")
    return choice

def new_chips():
    pringle = create_stack()
    for i in reversed(range(89)):
        push(pringle, i+1)
    
    
    
    return pringle

def eat():
    while True:
        #for list
        #print(f"Which can do you want to eat from: 1-{len(cans)}:")
        #can_number = int(input("selection:"))
        for key in cans:
            print(key)

        #picked_can = cans[can_number-1] for list
        choice = input("can:")
        picked_can = cans[choice]
        print("Eating...nom")
        pop(picked_can)
        left = size(picked_can)
        print(f"You have {left} chips left in the can.")
        again = input("Do you want to eat more?(Y/N):")
        if again.upper() == "Y":
            continue
        else:
            break

        
        
while True:
    choice = select_menu()
    if choice == "1":
        can = new_chips()
        color = input("color:") # for dictionary
        cans[color] = can #for dictionary
        #cans.append(can) #if list
        print(f"You bought a new pringle can. Now you have {len(cans)} pringle cans")
    elif choice == "2":
        eat()
