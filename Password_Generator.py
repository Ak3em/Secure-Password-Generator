import random
import string

#function to generate password (psd)
def psd_gen(min_length, include_num = True, include_Specialchar = True):

    letters = string.ascii_letters
    digits = string.digits
    specialchar = string.punctuation

    #source list for the potential characters of the password
    characters = letters
    if include_num:
        characters += digits
    if include_Specialchar:
        characters += specialchar

    #generate password and check if it satisfies the parameters
    psd = ""
    has_num = False
    has_Specialchar = False
    psdSet = False

    while not psdSet or len(psd) < min_length:
        new_char = random.choice(characters)
        psd += new_char
    #check if parameters are satisfied
        if new_char in digits:
            has_num = True
        if new_char in specialchar:
            has_Specialchar = True

        psdSet = True
        if include_num:
            psdSet = has_num
        if include_Specialchar:
            psdSet = psdSet and has_Specialchar

    return psd

def get_validInteger(prompt):
    while True:
        try:
            integer = int(input(prompt))
            if integer > 0:
                return integer
            else:
                print('Enter a number greater than 0.')
        except ValueError:
            print("Enter a valid integer.")


def get_validInput(prompt, valid_inputs):
    
    while True: 
        user_input = input(prompt).strip().lower()
        if user_input in valid_inputs:
            return user_input
        print("Invalid input, enter 'yes' or 'no'.")


while True:
    min_length = get_validInteger('Whats the least amount of characters the password should have? ')
    include_num = get_validInput("Should the password have numbers? (yes/no) ",['yes','no']) == 'yes'
    include_specialchar = get_validInput("Should the password have special characters? (yes/no) ", ['yes','no']) == 'yes'
    password = psd_gen(min_length, include_num, include_specialchar)
    print("Generated password:",password)
    repeat = input("Do you wanna generate another password? (yes/no) ").lower()
    if repeat != "yes":
        print("Thank you!!")
        break 
    
   



