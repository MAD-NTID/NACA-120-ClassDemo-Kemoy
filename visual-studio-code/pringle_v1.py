from stack import *


#Alex want to eat 3 chips... we will load 3 chips 
push("green")
push("blue")
push("purple")

print(f"The pringle can has {get_size()} chips")

print("Ragde decided to stole 2 chips and eat them")
pop() #nom
pop() #nom

print(f"Alex is left with:{get_size()} chips")
print(f"Justin peek in the can and he saw {get_top()} color chip")
print(f"Justin decided that he wanted to eat the {pop()} chip")

print(f"Alex decided he wanted to eat the chip. He look in the can and saw {get_size()}")
if is_empty():
    empty_word = "empty"
else:
    empty_word = "not empty"
print(f"Bruh.... He was maaaaaaad that it was {empty_word}")

