# Function to perform arithmetic operations
def calculate(x, operator, z):
    if operator == '+':
        return x + z
    elif operator == '-':
        return x - z
    elif operator == '*':
        return x * z
    elif operator == '/':
        return x / z

# Prompt the user for an arithmetic expression
expression = input("Expression: ")

# Split the input expression into x, operator, and z
x, operator, z = expression.split()

# Convert x and z to integers
x = int(x)
z = int(z)

# Calculate the result
result = calculate(x, operator, z)

# Print the result formatted to one decimal place
print(f'Result: {result:.1f}')
