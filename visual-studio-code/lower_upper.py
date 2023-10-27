words ="hello world, we are the best class. Fight me!"

print(words.lower())
print(words.upper())
print(words.capitalize())

target = input("search:")

for letter in words:
    if letter.lower() == target.lower():
        print("A match is found!")