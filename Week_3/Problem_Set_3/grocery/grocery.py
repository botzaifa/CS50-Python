def main():
    grocery_list = {}
    
    while True:
        try:
            item = input("Enter an item (Ctrl-D to finish input): ")
        except EOFError:
            break
        
        # Convert the item to lowercase to treat input case-insensitively
        item = item.lower()

        if item in grocery_list:
            grocery_list[item] += 1
        else:
            grocery_list[item] = 1

    # Sort the grocery list alphabetically
    sorted_items = sorted(grocery_list.keys())

    print("") # adding a new line
    for item in sorted_items:
        count = grocery_list[item]
        print(f"{count} {item.upper()}")

if __name__ == '__main__':
    main()


# TF Geometric intution
('''
A breakcdll Creates ()def e() finally getattr hasattr I java_ver(release='', vendor='', vminfo=, '', '', '') kbhit() L M nonlocal or pass 
quit raise Stime An idealized time(independent of any particular day, assuming that every day has exactly 24*60*60 seconds , there is no notion of "leap seconds" here)
ucd_3_2_0() varswindll Windows only: Creates () X yield zip

''')