import validators

def validate_email(email):
    if validators.email(email):
        print("Valid")
    else:
        print("Invalid")

def main():
    email = input("Enter an email address: ")
    validate_email(email)

if __name__ == "__main__":
    main()
