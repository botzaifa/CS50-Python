import inflect

def bid_adieu(names):
    p = inflect.engine()
    count = len(names)

    if count == 1:
        print(f"Adieu, adieu, to {names[0]}")
    elif count == 2:
        print(f"Adieu, adieu, to {names[0]} and {names[1]}")
    else:
        adieu_str = ", ".join(names[:-1])
        print(f"Adieu, adieu, to {adieu_str}, and {names[-1]}")

def main():
    names = [] # Array for storing all the names/input
    try:
        while True: # Print 'Name:' for every input
            name = input("Name: ")
            if not name:
                break
            names.append(name)
    except EOFError:
        pass  # Handle control-d to end input

    bid_adieu(names)

if __name__ == "__main__":
    main()
