pringle = []

def add_pringle(chip):
    pringle.insert(0, chip)

def eat():
    top = pringle.pop(0)
    return top

def pringle_size():
    return len(pringle)

def is_pringle_empty():
    return pringle_size() == 0

def top_pringle():
    return pringle[0]





#Alex want to eat 3 chips... we will load 3 chips 
add_pringle("green")
add_pringle("blue")
add_pringle("purple")

print(f"The pringle can has {pringle_size()} chips")

print("Ragde decided to stole 2 chips and eat them")
eat() #nom
eat() #nom

print(f"Alex is left with:{pringle_size()} chips")
print(f"Justin peek in the can and he saw {top_pringle()} color chip")
print(f"Justin decided that he wanted to eat the {eat()} chip")

print(f"Alex decided he wanted to eat the chip. He look in the can and saw {pringle_size()}")
if is_pringle_empty():
    empty_word = "empty"
else:
    empty_word = "not empty"
print(f"Bruh.... He was maaaaaaad that it was {empty_word}")