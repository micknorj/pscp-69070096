"""colors"""

a = input()
b = input()
c = ["Red", "Yellow", "Blue"]
if a in c and b in c:
    if (a == c[0] and b == c[1]) or (a == c[1] and b == c[0]):
        print("Orange")
    elif (a == c[0] and b == c[2]) or (a == c[2] and b == c[0]):
        print("Violet")
    elif (a == c[2] and b == c[1]) or (a == c[1] and b == c[2]):
        print("Green")
    else:
        print(a)
else:
    print("Error")
