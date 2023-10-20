"""
for num in range(5):
    print(num + 1)

for num in range(1,6):
    print(num)

for num in range(1,6,1):
    print(num)
"""
"""
for num in range(-1, 20):
    print(num + 1)
"""

"""
starting_number = int(input("Enter starting number:"))
stopping_number = int(input("Enter stopping number:"))

sum = 0
for num in range(starting_number, stopping_number):
    print(num)
    #sum  = sum + num
    sum+=num

print("Sum of all numbers: " + str(sum))
"""
""""
name = "RIT/NTID"

for letter in name:
    print(letter)

"""

#sentence = input("Enter the sentence:")

#target = input("Enter the word to search for:")

""""
word = ""
for letter in sentence:
    #print("current word: "+ word)
    if(word==""):
        word = letter
    
    elif(letter ==" "):
        if word == target:
            print(word + " found")
        else:
            word = ""
    else:
        word+=letter


    #print(letter)

"""

""""
delimeter = " "
words = sentence.split(delimeter)

count = 0
print(words)
for word in words:
    if target.lower() == word.lower():
        count+=1
        
print("A match was found for the word: "+ word + ". count:" + str(count))

"""
""""
EXIT_KEYWORD = "EXIT"
word = ""

while word!=EXIT_KEYWORD:
    word = input("Enter a word:")
    print("You type: "+ word)
"""

""""
PASS = "Shh$3cret"
word = ""

while word!=PASS:
    word = input("Enter the password:")
    if word == PASS:
        print("Welcome Admin")
    else:
        print("Incorrect password... I will block you!!!")
"""
""""
EXIT_KEYWORD = "EXIT"
while True:
    word = input("Enter a word:")
    print("You type: "+ word)

    if word == EXIT_KEYWORD:
        print("You entered EXIT.... I am terminating the loop. Bye....")
        break
"""

""""
sentence = input("Enter a sentence:")
target = input("Enter a target word to search:")
delimeter = " "
words = sentence.split(delimeter)

count = 0
for word in words:
    if target.lower() == word.lower():
        count+=1
        print("a match was found... we are breaking out")
        break
        
print("A match was found for the word: "+ word + ". count:" + str(count))
"""
""""
for num in range(1,10):
    if num%2!=0:
        continue

    print(num)
"""

LIMIT = 10
PASS = "S3cret"
tries = 0
blocked = False
while True:
    """"
    password = input("Enter password:")
    if password!=PASS:
        print("Incorrect password")
        continue
    """
    password = input("Enter password:")
    if password == PASS:
        break
    print("Incorrect password")
    tries+=1

    if tries == LIMIT:
        blocked = True
        print("BLOCKED")
        break

if not blocked:
    print("Welcome Admin")
else:
    print("You are blocked. Try again later")

