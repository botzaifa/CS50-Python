'''
Implement a program that prompts the user for a fraction, formatted as X/Y, wherein each of X and Y is an integer, 
and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank. 
If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty. 
And if 99% or more remains, output F instead to indicate that the tank is essentially full.
If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again. It is not necessary for Y to be 4. 
Be sure to catch any exceptions like ValueError or ZeroDivisionError.
Fuel gauges indicate, often with fractions, just how much fuel is in a tank. 
For instance 1/4 indicates that a tank is 25% full, 1/2 indicates that a tank is 50% full, and 3/4 indicates that a tank is 75% full.
'''


def get_fraction():
    while True:
        try:
            fraction = input("Enter a fraction (X/Y): ")
            x, y = map(int, fraction.split('/'))
            if y == 0 or x > y:
                raise ValueError
            return x, y
        except (ValueError, ZeroDivisionError):
            print("Invalid input. Please enter a valid fraction (X/Y) where X and Y are integers, Y is not zero, and X <= Y.")

def calculate_fuel_percentage(x, y):
    fuel_percentage = (x / y) * 100
    return round(fuel_percentage)

while True:
    x, y = get_fraction()
    fuel_percentage = calculate_fuel_percentage(x, y)

    if fuel_percentage <= 1:
        print("E")
    elif fuel_percentage >= 99:
        print("F")
    else:
        print(f"Fuel tank is {fuel_percentage}% full.")
    
    another = input("Do you want to check another fraction? (yes/no): ").lower()
    if another != 'yes':
        break
