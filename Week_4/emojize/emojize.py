import emoji

def emojize_text(input_text):
    alias_mapping = {
        ":thumbsup:": "👍",
        ":smile:": "😊",
        ":earth_asia:": "🌏",
        ":1st_place_medal:": "🥇",
        ":candy:": "🍬",
        ":ice_cream:": "🍨"
    }

    for alias, emoji_char in alias_mapping.items():
        input_text = input_text.replace(alias, emoji_char)

    return input_text

def main():
    user_input = input("")
    emojized_output = emojize_text(user_input)
    print("", end='')  # Ensure the output is printed on the same line
    print(emojized_output)

if __name__ == "__main__":
    main()
