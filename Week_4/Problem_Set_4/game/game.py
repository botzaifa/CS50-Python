import random

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
                return level
        except ValueError:
            pass

def get_guess():
    while True:
        try:
            guess = int(input("Guess: "))
            if guess > 0:
                return guess
        except ValueError:
            pass

def main():
    level = get_level()
    secret_number = random.randint(1, level)

    while True:
        guess = get_guess()

        if guess < secret_number:
            print("Too small!")
        elif guess > secret_number:
            print("Too large!")
        else:
            print("Just right!")
            break

if __name__ == "__main__":
    main()
