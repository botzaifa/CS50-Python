import random

def main():
    level = get_level()
    score = run_quiz(level)
    print(f"Score: {score}")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in {1, 2, 3}:
                return level
        except ValueError:
            pass

def generate_integer(level):
    if level not in {1, 2, 3}:
        raise ValueError()
    
    if level == 3:
        return random.randint(100, 999)
    elif level == 2:
        return random.randint(10,99)
    else:
        return random.randint(0, 10**level - 1)

def run_quiz(level):
    score = 0
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        correct_answer = x + y

        for _ in range(3):
            user_answer = input(f"{x} + {y} = ")
            try:
                user_answer = int(user_answer)
                if user_answer == correct_answer:
                    score += 1
                    break
                else:
                    print("EEE")
            except ValueError:
                print("EEE")
        else:
            print(correct_answer)

    return score


if __name__ == "__main__":
    main()
