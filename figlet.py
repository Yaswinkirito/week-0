import sys
import pyfiglet

name = input("what to display: ")
print(pyfiglet.figlet_format(f"{name}", font=f"{sys.argv[1]}"))
