"""round to the nearest 10"""

number = int(input())
number = (number // 10) * 10
space = []
while number / 10 >= 0:
    space.append(number)
    number -= 10
print(*space)
