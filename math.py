n=input()
x , y ,z =n.split(sep=" ")
x=int(x)
z=int(z)
if y=="*":
    print(f"{x*z}")
elif y=="/":
    print(f"{x/z}")
elif y=="-":
    print(f"{x-z}")
else:
    print(f"{x+z}")

