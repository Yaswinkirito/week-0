def main():  # assign meal
    t = clock()
    if 7.00 <= t <= 8.00:
        print("It's breakfast time")
    elif 12.00 <= t <= 13.00:
        print("It's lunch time")
    elif 18.00 <= t <= 19.00:
        print("It's dinner time")
    else:
        print("")


def clock():
    time = input("what time is it ? ")  # inputs time
    h, m = time.split(sep=":")
    t = int(h) + (int(m) / 60)
    return t


main()
