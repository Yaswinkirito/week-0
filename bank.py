greet = input("Greeting: ")
if "hello" in greet.lower():
    print("$0")
elif "h" in greet[0].lower():
    print("$20")
else:
    print("$100")
