"""
    Author: Kemoy Campbell
    Purpose:
        This program is a login program.
        If the user enter the right username and password
        they have access to the system
        otherwise access denied
"""


'''
    Set up two constants with the right username and password
'''
PASSWORD = "topS3cret"
USERNAME = "lordy"


#Ask the user for the password
password = input("Enter your password:")

#ask the user for the for username
username = input("Enter your username:")

#check if the password and username match
if (PASSWORD == password and USERNAME == username):
    #the username and password match so we let them in
    print("Welcome star lord")
else:
    #didnt match... go away!!
    print("access denied")

