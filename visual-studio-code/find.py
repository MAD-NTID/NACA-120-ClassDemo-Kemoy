words ="Hello world, we are the best class. Fight me!"

index = words.find("b")
print("B is at index:",index)

print(words[index])
index = words.find("e")
print("e is at:", index)


def find_all(word,target):
    indexes = []
    for i in range(len(word)):
        if word[i] == target:
            indexes.append(i)
    
    return indexes

index = find_all(words, "e")
print("e is at index:",index)

index = words.find("j")
print("j is at ", index)




