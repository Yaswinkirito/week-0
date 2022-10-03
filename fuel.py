def main():
    f = input("x/y: ").split(sep="/")
    errorcheck(f)
    response(f)


def errorcheck(e):  # checks for error in input
    e[0] = int(e[0])
    e[1] = int(e[1])
    if e[1] == 0 or e[0] > e[1]:
        main()
    return


def response(e):  # returns response to input
    p = (int(e[0]) / int(e[1])) * 100
    if float(p % 1) < 0.5:
        r = int(p // 1)
    else:
        r = int(p // 1) + 1
    if r <= 1:
        print("Nearly empty")
    elif r >= 99:
        print("Full")
    else:
        print(f"{r}% full")


try:  # input error
    main()
except ValueError:
    print("Invalid input")
