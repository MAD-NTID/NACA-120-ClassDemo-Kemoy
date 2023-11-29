def has_name_loop(list_names, target_name):
    for name in list_names:
        if name.lower() == target_name.lower():
            return True

    return False

names = ["Kratos","Pikachu", "Master Chief", "Gordon Ramsey", "I am a sandwich"]
target = "Gordon Ramsey"

found = has_name_loop(names, target)
print("Found?:", found)

found = has_name_loop(names, "Donald Trump")
print("Found?:", found)

def has_name_rec(name_list, target_name):
    if len(name_list) == 0:
        return False
    name = name_list[0]
    if name.lower() == target_name.lower():
        return True
    return has_name_rec(name_list[1:], target_name)

def has_name_rec_2(name_list, target_name, index):
    if index < 0:
        return False
    name = name_list[index]

    if name.lower() == target_name.lower():
        return True

    return has_name_rec_2(name_list, target_name, index-1)

found = has_name_rec(names, "Gordon Ramsey")
print("Found?:", found)
    
found = has_name_rec(names, "Donald Trump")
print("Found?:", found)

found = has_name_rec_2(names, "Gordon Ramsey", len(names)-1)
print("Found?:", found)
found = has_name_rec_2(names, "Donald Trump", len(names)-1)
print("Found?:", found)


found = has_name_rec_2(names, "Donald Trump", None)
print("Found?:", found)


