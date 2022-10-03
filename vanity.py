def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):    #checks validity
    if num(s)==num2(s)==spec(s)==True:
        return True
    else:
        return False

def num(l):               #checks for charcter limit
    if 6<len(l)<2:
        return False
    else:
        return True


def spec(q): #checks for periods and spaces
    for r in q:
        if r in  ["."," "] :
            
            return False
        
    return True

    
        
def num2(q):     #checks whether the string satisfies the condition of vanity plate numbers part
    m=0
    for i in range(0,len(q)):
        try:
            int(q[i])
            if m==0:
                if int(q[i])==0:
                    return False
                else:
                    m=+1
                


        except ValueError:
            if(i==(len(q)-1)):
                return False

    return True

        


    


main()