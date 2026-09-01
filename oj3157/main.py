"""points collection"""

turn = int(input())
value = 0

for _ in range(turn):
    action = input()
    if action == "+":
        value += 10
    else:
        value -= 5

print(value)
