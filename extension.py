file=(input("enter file name? ")).lower()
print(file)
if ".gif" in file:
    print("images/gif")
elif ".jpg" in file:
    print("images/jpg")
elif ".jpeg" in file:
    print("images/jpeg")
elif ".png" in file:
    print("images/png")
elif ".pdf" in file:
    print("application/pdf")
elif ".txt" in file:
    print("text/plain")
elif ".zip" in file:
    print("application/zip")
else:
    print("application/octet-stream")
    
        

    