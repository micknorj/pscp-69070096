"""brick calculator"""

small = int(input())
big = int(input())
goal = int(input())
if big * 5 == goal:
    print("0")
elif big * 5 > goal:
    if goal % 5 <= small:
        print(goal % 5)
    else:
        print("-1")
elif big * 5 < goal:
    if (big * 5) + small >= goal:
        print(goal - (big * 5))
    else:
        print("-1")
