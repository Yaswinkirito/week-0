d = input("Date:")
m = [
    "january",
    "febuary",
    "march",
    "april",
    "may",
    "june",
    "july",
    "august",
    "september",
    "october",
    "november",
    "december",
]
if "/" in d:
    x, y, z = d.split(sep="/")
    print(f"{z}/{x}/{y}")
else:
    d = d.lower()
    x, y, z = d.split(",")
    if y in m:
        print(f"{y},{x},{z}")
