name=[]
task=input("say something? ")
l=int(len(task))
for q in task:
    name.append(q)
for names in name:
    if "A"<=names<="Z":
        names=names.lower()
        print(f"_{names}",end="")
    else:
        print(names,end="")