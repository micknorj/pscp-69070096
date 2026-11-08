"""3477"""

INGREDIENTS = {
    "Pad Thai Sauce",
    "Tofu",
    "Pickle Turnip",
    "Shrimp",
    "Bean Sprouts",
    "Noodle",
    "Chives",
    "Lime",
    "Egg",
    "Oil",
    "Peanuts"
}

TASTES = {"Sweet", "Sour", "Salty"}

ingredients = set()
tastes = set()

while True:
    item = input()
    if item == "Cook":
        break
    ingredients.add(item)

while True:
    taste = input()
    if taste == "End":
        break
    tastes.add(taste)

if not ingredients.issubset(INGREDIENTS):
    print("This is not Pad Thai!!!")
elif ingredients != INGREDIENTS:
    print("This is bad!")
elif tastes != TASTES:
    print("Not Bad...")
else:
    print("Delicious!")
