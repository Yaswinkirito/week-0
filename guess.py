import random
import sys

number = random.randint(1, 100)


def main():
    while True:
        i = int(input("guess a number "))
        if i < 0:
            pass
        elif i > number:
            print("Too large!")
            pass
        elif i < number:
            print("Too small!")
            pass
        else:
            print("close!")
            sys.exit()


main()
