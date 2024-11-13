x = input("Greeting: ")

y = x.lower().strip()

if y.startswith("hello"):
    print("$0")
    
elif y.startswith("h"):
    print("$20")
    
else:
    print("$100")