"""frog"""

x, y = map(int, input().split())
count = 0
distance = 0

while distance < y:
    if x <= 0:
        count = -1
        break
    distance += x
    count += 1
    x -= 2

print(count)
