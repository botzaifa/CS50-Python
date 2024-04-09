def convert(input_str):
    #Function for replacing the Symbols to emoji
    input_str = input_str.replace(":)", "🙂").replace(":(", "🙁")
    return input_str
    
def main():
    x = input("Enter your text here: ")
    result = convert(x)
    print("The converted string is: ", result)
    
    
if __name__ == "__main__":
    main()