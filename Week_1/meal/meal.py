def main():
    # Get the user's input for the time in 24-hour format
    time_input = input("Enter the time (HH:MM): ")

    # Call the convert function to convert the input time to hours
    try:
        hours = convert(time_input)
    except ValueError:
        print("Invalid time format. Please use HH:MM format.")
        return

    # Define the meal time ranges
    breakfast_start = 7.0
    breakfast_end = 8.0
    lunch_start = 12.0
    lunch_end = 13.0
    dinner_start = 18.0
    dinner_end = 19.0

    # Check if the time falls within the meal time ranges and output the meal
    if breakfast_start <= hours <= breakfast_end:
        print("breakfast time")
    elif lunch_start <= hours <= lunch_end:
        print("lunch time")
    elif dinner_start <= hours <= dinner_end:
        print("dinner time")

def convert(time):
    # Split the time string into hours and minutes
    hours_str, minutes_str = time.split(":")

    # Convert hours and minutes to integers
    hours = int(hours_str)
    minutes = int(minutes_str)

    # Calculate the total hours as a float
    total_hours = hours + minutes / 60.0

    return total_hours

if __name__ == "__main__":
    main()
