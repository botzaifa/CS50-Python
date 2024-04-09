import re

def camel_to_snake(camel_str):
    # Use regular expressions to split the camelCase string
    words = re.findall(r'[A-Za-z][a-z]*', camel_str)
    # Join the words with underscores and convert to lowercase
    snake_case_str = '_'.join(words).lower()
    return snake_case_str


camel_case_str = input("camelCase: ")
snake_case_str = camel_to_snake(camel_case_str)
print("camelCase:", camel_case_str)
print("snake_case:", snake_case_str)
