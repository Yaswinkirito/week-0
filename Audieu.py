names = []


def main():
    try:
        while True:
            names.append(input("Name: "))
            l = len(names)
    except EOFError:
        print("Audieu,audieu,", end="")
        for i in range(0, l):
            if i != (l - 1):
                print(names[i], end=",")
            else:
                print(f"and {names[i]}", end="")


main()
