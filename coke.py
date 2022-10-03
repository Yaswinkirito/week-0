amount=50
while amount>0:
    print(f"balance amount {amount}")
    balance=int(input("enter amount: "))
    if balance in [50,25,10,5]:
        amount=amount-balance
        if amount >=0:
            print(f"balance amount: {amount}")
        else:
            print(f"change: {-amount}")
    