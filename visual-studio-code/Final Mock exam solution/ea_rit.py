import re

# Predefined variables
games_records = [] #this will keep a list of all game sales

# Predefined function
def display_menu():
    print("Menu Options:")
    print("1. Create a new sale")
    print("2. Remove a record")
    print("3. Show all sales")
    print("4. Filter sale by platform")
    print("5. Exit")
    
# Predefined function
def menu_selection():
    display_menu()
    while True:
        try:
            choice = int(input("Enter your choice (1-5): "))
            if choice < 1 or choice > 5:
                print("Invalid choice. Please enter a number between 1 and 5.")
                continue
            
            return choice
                
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            
# functions to be completed by the student goes here
def is_valid_date(date):
    regex = r'^\d{2}-\d{2}-\d{4}$'
    #match = re.match(regex,date)
    return bool(re.match(regex,date))
    """"
    if match is not None:
        return True
    return False
    """

def create_sale():
    name = input("Game name:")
    platform = input("Game platform:")
    while True:
        date = input("Date sale:")
        if not is_valid_date(date):
            print("Invalid date")
            continue
        break
    cost = float(input("Game cost:"))

    record = {"name":name, "platform":platform, "date":date, "cost":cost}
    games_records.append(record)
    print("Game record successfully added")

def remove_record():
    name = input("Enter the name of the game to remove:")
    platform = input("Enter the name of the platform to remove:")

    #loop through the list
    #old_size = len(games_records)
    deleted = False
    for record in games_records:
        #find the matching name and platform
        if record["name"] == name and record["platform"] == platform:
            games_records.remove(record) # remove the matching record
            print("Record successfully remove")
            deleted = True
            break
    
    if deleted == False:
        print("Nothing was deleted as no match was found")
    # if old_size==len(games_records):
    #     print("No match found")
def show_sales():
    if len(games_records) == 0:
        print("Empty record")
    else:
        for record in games_records:
            print(record)

def filter_by_platform_rec(record_list, target, filtered_list):
    if len(record_list) == 0:
        return filtered_list
    
    #get the dictionary out of the list for index 0
    record = record_list[0]
    #search for match platform
    if record["platform"] == target:
        filtered_list.append(record) #move the match to the filtered list
    
    #update our record to focus on the next items in the list and dont include old 0
    record_list = record_list[1:]

    #do it again
    return filter_by_platform_rec(record_list, target, filtered_list)

def filter_by_platform_rec_with_index(record_list, target, filtered_list, index):
    if index > len(record_list):
        return filtered_list
    
    #get the dictionary out of the list for index 0
    record = record_list[index]
    #search for match platform
    if record["platform"] == target:
        filtered_list.append(record) #move the match to the filtered list
    
    return filter_by_platform_rec_with_index(record_list, target, filtered_list, index+1)

def filter_by_platform():
    platform = input("Enter the platform to filter by:")
    filtered_list = []
    filtered = filter_by_platform_rec(games_records, platform, filtered_list)

    for record in filtered:
        print(record)
def main():
    while True:
        try:
            selection = menu_selection()
            if selection == 1:
                create_sale()
            elif selection == 2:
                remove_record()
            elif selection == 3:
                show_sales()
            elif selection == 4:
                filter_by_platform()
            else:
                print("Thank you for using RIT EA store")
                break
        except:
            print("Invalid action")
    

#test
# print(is_valid_date("12-12-2023"))
# print(is_valid_date("A-12-2023"))
# create_sale()
# print(games_records)
if __name__ == "__main__":
    main()