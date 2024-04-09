'''
Implement a program that prompts the user for a vanity plate and then output Valid if meets all of the requirements or Invalid if it does not. 
Assume that any letters in the user's input will be uppercase. 
Structure your program per the below, wherein is_valid returns True if s meets all requirements and False if it does not. 
Assume that s will be a str. You're welcome to implement additional functions for is_valid to call (e.g., one function per requirement).

Conditions:
“All vanity plates must start with at least two letters.”
“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. 
The first number used cannot be a '0'.
“No periods, spaces, or punctuation marks are allowed.”

'''

def is_valid(s):
    """Returns True if the given string is a valid Massachusetts vanity license plate, False otherwise."""

    # Check if the string is at least 2 characters long.
    if len(s) < 2:
        return False

    # Check if the first number used cannot be a '0'.
    if s.isdigit() and s[0] == '0':
        return False

    if s[2] == '0':
        return False

    # Check if the string starts with at least 2 letters.
    if not s[:2].isalpha():
        return False

    # Check if the string contains only letters and numbers.
    if not s.isalnum():
        return False

    # Check if numbers cannot be used in the middle of a plate.
    for i in range(len(s) - 1):
        if s[i].isdigit() and s[i + 1].isalpha():
            return False

    # Check if the string is a maximum of 6 letters.
    if len(s) > 6:
        return False

    # All requirements met.
    return True

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__":
    main()
