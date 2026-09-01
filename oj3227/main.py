"""Cards"""

CARDS = {
    "A" : "ace",
    "J" : "jack",
    "Q" : "queen",
    "K" : "king"
}

FACES = {
    "C" : "clubs",
    "D" : "diamonds",
    "H" : "hearts",
    "S" : "spades"
}

card = input().upper()
x = card[:-1]
y = card[-1]

if card[:-1] in CARDS:
    x = CARDS[card[:-1]]
if card[-1] in FACES:
    y = FACES[card[-1]]

print(f"{x} of {y}")
