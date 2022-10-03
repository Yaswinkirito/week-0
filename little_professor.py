import random, sys


def main():
    d = get_level(int(input("Enter level: ")))
    x = d[0]
    y = d[1]
    for i in range(0, 3):
        answer = int(input(f"{x}+{y}= "))
        if answer == x + y:
            print("correct")
            sys.exit()
        else:
            print("Incorrect")
    print(x + y)


def get_level(a):
    if a not in range(0, 4):
        print("invalid level")
    else:
        return generate_integer(a)


def generate_integer(level):
    if level == 1:
        b = random.randint(0, 9)
        c = random.randint(0, 9)
    elif level == 2:
        b = random.randint(10, 99)
        c = random.randint(10, 99)
    else:
        b = random.randint(100, 999)
        c = random.randint(100, 999)
    d = [b, c]
    return d


if __name__ == "__main__":
    main()
