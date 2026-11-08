"""3293"""

first = input().rstrip()
second = input().rstrip()
third = input().rstrip()
fourth = input().rstrip()
fifth = input().rstrip()

width = 0

for text in (first, second, third, fourth, fifth):
    if len(text) > width:
        width = len(text)

print("*" * (width + 4))

for text in (first, second, third, fourth, fifth):
    print("* " + text.ljust(width) + " *")

print("*" * (width + 4))
