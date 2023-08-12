

def star(No):
    if(No > 0):
        print("*",end=" ")
        No = No - 1
        star(No)

star(5)