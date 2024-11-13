def main():
    try:
        fraction = input("Enter the fuel fraction in X/Y format: ")
        percentage = convert(fraction)
        result = gauge(percentage)
        print(result)
    except (ValueError, ZeroDivisionError) as e:
        print(e)


def convert(fraction):
    x, y = map(int, fraction.split('/'))
    if not isinstance(x, int) or not isinstance(y, int):
        raise ValueError("X and Y must be integers")
    if x > y:
        raise ValueError("X must be less than or equal to Y")
    if y == 0:
        raise ZeroDivisionError("Y cannot be 0")
    return round((x / y) * 100)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
