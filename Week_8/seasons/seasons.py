from datetime import date
import inflect
import sys
import operator

p = inflect.engine()

def main():
    try:
        dob = input("Date of Birth: ")
        diff = operator.sub(date.today(), date.fromisoformat(dob))
        print(convert(diff.days))
    except ValueError:
        sys.exit("Invalid date")

def convert(time):
    m = time * 24 * 60
    return f"{(p.number_to_words(m, andword='')).capitalize()} minutes"

if __name__ == "__main__":
    main()
