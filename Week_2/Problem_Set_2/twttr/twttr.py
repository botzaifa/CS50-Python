'''
implement a program that prompts the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted, 
whether inputted in uppercase or lowercase.
'''

# Prompt the user for input
user_input = input("Enter a string of text: ")

# Define a string containing all vowels (both uppercase and lowercase)
vowels = "AEIOUaeiou"

# Initialize an empty string to store the result
result = ""

# Loop through each character in the user input
for char in user_input:
    # Check if the character is not a vowel and add it to the result
    if char not in vowels:
        result += char

# Print the result without vowels
print("Text with vowels removed:", result)
