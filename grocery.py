try:
    list = []
    k = ""
    while True:
        k = input("Item ")
        list.append(k.strip())
        list = sorted(list)
except EOFError:
    for item in list:
        n = list.count(item)
        print(f"{n} {item.upper()}")
        list.remove(item)
