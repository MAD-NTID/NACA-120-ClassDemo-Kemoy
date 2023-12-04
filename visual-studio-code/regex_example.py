import re

#REGEX re.search example
""""
regex = r'\d+'
data = "Trent123"
match = re.search(regex, data)
if match is None:
    print("No match found")
else:
    print("a match was found:" + match.group())
"""

#re.match example
""""
sentence = "Hello, Welcome to RIT!"
regex = r'Hello'
match = re.match(regex, sentence)
print(match.group())

def start_with(start,text):
    regex = r'' + start
    match = re.match(regex, text)
    if match is None:
        return False
    else:
        return True

test_text = "Welcome to RIT"
result = start_with("RIT",test_text)
print(result)
"""
""""
def is_digit(text):
    regex = r'^\d+$'
    match = re.search(regex, text)#re.match(regex, text)#re.search(regex, text)
    return bool(match)

test_evil = "1234"
result = is_digit(test_evil)
print(result)
"""

numbers = """RIT has many phone numbers. Here are some
        numbers we use on campus:
        123-254-3698
        569-2351245
        1235698745
        (123)-584-2369
        4444
        """


""""
def extract_phone_number(data):
    regex = r'\(?\d{3}\)?-?\d{3}-?\d{4}'
    matches = re.findall(regex, data)
    return matches

result = extract_phone_number(numbers)
print(result)

def is_valid_phone_number(number):
    numbers = extract_phone_number(number)
    if len(numbers) > 0:
        return True
    else:
        return False
    #return len(extract_phone_number(number)) > 0

while True:
    number = input("Enter phone number:")
    if not is_valid_phone_number(number):
        print("Invalid number!!!")
        continue
    break
"""

def show_last_four_ssn(ssn):
    regex = r'\d{3}-?\d{2}-?'
    replacement = "***-**-"
    last_four = re.sub(regex, replacement, ssn)
    return last_four

while True:
    ssn = input("Enter your ssn:")
    last_four = show_last_four_ssn(ssn)
    print("The last 4 of your ssn is:" + last_four)
