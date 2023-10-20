def divide(num1, num2):
    if num2 == 0:
        return 0
    
    result = num1 /  num2
    return result



while True:
    first = input("Enter the first number:")
    second = input("Enter the second number:")

    if not second.isdigit() or not first.isdigit():
        print("Really bruh?! numbers only")
        continue

    first = int(first)
    second = int(second)

    result = divide(first, second)
    print("Result:", result)

    if(input("Do you want to do another calculation:")== 'N'):
        print("Thank you for using this calculation...goodbye")
        break

