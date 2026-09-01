"""season check"""

month = int(input())
date = int(input())
if 1 <= month <= 3:
    if not month % 3 and date >= 21:
        print("spring")
    else:
        print("winter")
if 4 <= month <= 6:
    if not month % 3 and date >= 21:
        print("summer")
    else:
        print("spring")
if 7 <= month <= 9:
    if not month % 3 and date >= 21:
        print("fall")
    else:
        print("summer")
if 10 <= month <= 12:
    if not month % 3 and date >= 21:
        print("winter")
    else:
        print("fall")
