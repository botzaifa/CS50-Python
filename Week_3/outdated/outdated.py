from datetime import datetime

def is_valid_date(date):
    try:
        datetime.strptime(date, "%m/%d/%Y")
        return True
    except ValueError:
        try:
            datetime.strptime(date, "%B %d, %Y")
            return True
        except ValueError:
            return False

def format_to_iso(date):
    try:
        parsed_date = datetime.strptime(date, "%m/%d/%Y")
    except ValueError:
        parsed_date = datetime.strptime(date, "%B %d, %Y")
    return parsed_date.strftime("%Y-%m-%d")

while True:
    user_input = input("Enter a date: ").strip()
    if is_valid_date(user_input):
        formatted_date = format_to_iso(user_input)
        print(f"Formatted date: {formatted_date}")
        break
    else:
        print("Invalid date format. Please enter a valid date.")
