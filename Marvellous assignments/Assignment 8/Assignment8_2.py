

def number(No):
    if (No > 0):
        number(No - 1)
        print(No, end=" ")

number(5)