
# Menu dictionary with menu items and their prices
menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

# Initialize an empty list to store the user's order
order = []

# Function to calculate the total cost of the order
def calculate_total(order):
    total = sum(menu[item] for item in order)
    return total

try:
    print("Item: ")

    while True:
        item = input().strip().title()  # Read and titlecase the user's input

        # Check if the item is in the menu
        if item in menu:
            order.append(item)  # Add the item to the order list
            total_cost = calculate_total(order)  # Calculate the total cost
            print(f"Total: ${total_cost:.2f}")  # Display the total cost
        else:
            print("Item not found on the menu. Please enter a valid menu item.")
except EOFError:
    # Handle the end of input (Ctrl-D) gracefully
    print("\nThank you for placing your order!")
    total_cost = calculate_total(order)
    print(f"Your total cost is: ${total_cost:.2f}")
