"""
@author: Kemoy Campbell
date: 11/01/2023
Project code name: MathWiz
Purpose:
    MathWiz is  online mathematics platform, offering players the opportunity to test their mathematical skills 
    while being rewarded with XP for each correct answer. What sets MathWiz apart is its dynamic XP system, 
    where XP is generated randomly and multiplies with each advancing round. The adventure begins at round 1 
    and progresses with every accurate response. In your role as a software engineer, 
    you've been handpicked to lead the design and development of the MathWiz platform, 
    bringing this unique mathematical experience to life.
"""

#PREDEFINED
import random
import datetime

MIN_NUMBER = 0
MAX_NUMBER = 10


#PREDEFINED
"""
    This function generate an xp.
    The function first generate an xp
    then multiply that by the round number

    Parameter:
        round: The current round in the game
"""
def generate_xp(round):
    min_xp = 3
    max_xp = 10
    xp = random.randint(min_xp, max_xp)
    return xp * round

#PREDEFINED
"""
    This function will generate a random number from 0 - 10
    returns the number that was generated
"""
def generate_a_number():
    return float(random.randint(MIN_NUMBER, MAX_NUMBER))

#PREDEFINE
"""
    This function will print MathWiz as well as today's date and time
"""
def game_header():
    print("===========================================================================\n")
    print("||\\\\   //||    //\\\\   |```````|  ||    ||   \\\\          // ||  =====")
    print("|| \\\\ // ||   //==\\\\   ``| |``   ||====||    \\\\  //\\\\  //  ||   //")
    print("||  \\\\// ||  //    \\\\    | |     ||    ||     \\\\//  \\\\//   ||  //=====")
    print("\n===========================================================================")
    now = datetime.datetime.now()
    print("Date and Time:",now.strftime("%d/%m/%Y %H:%M:%S"))
#PREDEFINED
"""
    This function will returns a random math operation.
    The operation will be one of the following +, -, / or *
"""
def generate_math_operation():

    #Type of operations supported
    operations = ["+", "-", "/", "*"]

    # randomly pick one of the operations
    # from the supported operations and return it
    min_index = 0
    max_index = len(operations)-1
    index = random.randint(min_index, max_index)
    
    picked_operation = operations[index]

    return picked_operation

#FUNCTION CODES HERE
def add(number1, number2):
    return number1 + number2

def subtract(number1, number2):
    return number1 - number2

def divide(number1, number2):
    return number1/ number2

def multiply(number1, number2):
    return number1 * number2

def generate_second_number(operation):
    while True:
        num2 = generate_a_number()
        if operation == "/" and num2 == 0:
            continue
        else:
            return num2
def get_user_answer():
    while True:
        answer = input("Answer:")
        if answer == "quit":
            return answer
        else:
            try:
                answer = float(answer)
                return answer
            except ValueError:
                print("Answer must be digit or quit")

#STUDENT CODE HERE

#PREDEFINED
def main():
    total_xp = 0
    round = 1
    question = ""
    answer = ""
    total_correct_answer = 0
    total_wrong = 0
    while True:
        try:
            #STUDENT CODE HERE
            game_header()

            print("Round:", round)
            print("Total xp:", total_xp)
            print("previous question:", question)
            print("previous answer:", answer)
            print("Stat\n======")
            print("Total correct answers:", total_correct_answer)
            print("Total incorrect answers:", total_wrong)

            operation = generate_math_operation()
            num1 = generate_a_number()
            num2 = generate_second_number(operation)
            
            #ask the user the question
            print("What is the answer for:")
            question = f"{num1}{operation}{num2}"
            print(question)

            answer = get_user_answer()
            if answer == "quit":
                print("Thank you for playing. See you again soon!")
                break
            
            #check for right answers
            if operation == "/":
                correct_answer = divide(num1,num2)
            elif operation == "+":
                correct_answer = add(num1, num2)
            elif operation == "-":
                correct_answer = subtract(num1, num2)
            else:
                correct_answer = multiply(num1, num2)
            
            #check user's answer with computer's answr
            if answer == correct_answer:
                print("Yay you got it")
                xp = generate_xp(round)
                print(f"You got {xp} for this round!")
                total_xp +=xp
                print(f"Your total xp is now {total_xp}")
                total_correct_answer+=1
            else:
                print("Nope, you are wrong")
                print("The correct answer is", correct_answer)
                total_wrong+=1
            round+=1
        except:
            print("An odd error happened. Please try again")


#PREDEFINED
main()

    