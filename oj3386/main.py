"""3386"""

m = int(input())
n = int(input())

group1 = {int(input()) for _ in range(m)}
group2 = {int(input()) for _ in range(n)}

common = sorted(group1 & group2, reverse=True)

if common:
    for student in common:
        print(student)
else:
    print("Nope")
