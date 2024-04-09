import sys
import random
from pyfiglet import Figlet

def get_random_font():
    figlet = Figlet()
    fonts = figlet.getFonts()
    return random.choice(fonts)

def print_invalid_usage_and_exit():
    print("Invalid usage")
    sys.exit(1)

def validate_font(font_name):
    figlet = Figlet()
    valid_fonts = figlet.getFonts()
    if font_name not in valid_fonts:
        print("Invalid usage")
        sys.exit(1)

def main():
    if len(sys.argv) == 1:
        font_name = get_random_font()
    elif len(sys.argv) == 3 and (sys.argv[1] == '-f' or sys.argv[1] == '--font'):
        font_name = sys.argv[2]
        validate_font(font_name)
    else:
        print_invalid_usage_and_exit()

    user_input = input("Input: ")

    figlet = Figlet(font=font_name)
    output_text = figlet.renderText(user_input)

    print("Output:")
    print(output_text)

if __name__ == '__main__':
    main()
