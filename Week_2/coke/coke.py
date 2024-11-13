'''
implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due. 
Once the user has inputted at least 50 cents, output how many cents in change the user is owed. 
Assume that the user will only input integers, and ignore any integer that isn't an accepted denomination.
Suppose that a machine sells bottles of Coke for 50 cents and only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.
'''

def print_amount_due(amount_due):
    print(f"Amount Due: {amount_due}")

def insert_coin(total_inserted, amount_due):
    while True:
        try:
            coin = int(input("Insert coin: "))
        except ValueError:
            print("Please insert a valid coin.")
            continue

        if coin in accepted_denominations:
            total_inserted += coin
            amount_due -= coin
            if amount_due > 0:
                print_amount_due(amount_due)
            elif amount_due == 0:
                print("Change Owed: 0")
            else:
                change = abs(amount_due)
                print(f"Change Owed: {change}")
            return total_inserted, amount_due
        else:
            print_amount_due(amount_due)

# Initialize variables
amount_due = 50
total_inserted = 0
accepted_denominations = [25, 10, 5]

print_amount_due(amount_due)

# Prompt the user to insert coins until at least 50 cents are inserted.
while total_inserted < 50:
    total_inserted, amount_due = insert_coin(total_inserted, amount_due)

# Display the total change owed if any.
if total_inserted > 50:
    change = total_inserted - 50
    print(f"Change Owed: {change}")
