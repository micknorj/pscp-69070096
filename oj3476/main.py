"""3476"""
import ast

n = int(input())
animals = {}

for _ in range(n):
    animals.update(ast.literal_eval(input()))

if "Garfield" not in animals and "Cat01" not in animals.values():
    animals["Garfield"] = "Cat01"

if "Fubuki" not in animals and "Fox01" not in animals.values():
    animals["Fubuki"] = "Fox01"

cats = sorted(
    ((name, code) for name, code in animals.items()
     if code.startswith("Cat")),
    key=lambda x: int(x[1][3:])
)

foxes = sorted(
    ((name, code) for name, code in animals.items()
     if code.startswith("Fox")),
    key=lambda x: int(x[1][3:])
)

print(f"Cat : {len(cats)}")
print(f"Fox : {len(foxes)}")

for name, code in cats + foxes:
    print(f"{name} : {code}")
