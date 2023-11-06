cart = []

def add_to_cart():
    item = input("Enter item name:")
    quantity = int(input("Enter quantity:"))

    tuple_item = (item, quantity)
    cart.append(tuple_item)
    print("Item added to cart")

def view_cart():
    print("Your cart:\n========")
    for stuff in cart:
        print(stuff)

def update_item():
    target = input("Enter the item to update:")
    quantity = int(input("Enter the new quantity:"))

    for i in range(len(cart)):
        stuff = cart[i]
        if stuff[0] == target:
            new_stuff = (stuff[0], quantity)
            #overwrite the previous stuff in the cart at the specific index
            cart[i] = new_stuff
            print("successful updated")
            break

while True:
    print("Menu\n======")
    print("1.Add item")
    print("2.Update item")
    print("3.View Cart")
    print("4.Exit")

    choice = input("Choice:")
    if choice == "1":
        add_to_cart()
    elif choice=="2":
        update_item()
    elif choice == "3":
        view_cart()


