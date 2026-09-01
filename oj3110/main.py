"""delivery with conditions"""

ROUTES = {
    ("BKK", "CNX"): (10, 30),
    ("BKK", "PKT"): (25, 50),
    ("CNX", "UBP"): (15, 40),
    ("UBP", "BKK"): (20, 40),
    ("PKT", "CNX"): (30, 60),
    ("UBP", "PKT"): (40, 70),
}
front, end = input().split()
weight = float(input())
if (front, end) in ROUTES:
    base, rate = ROUTES[(front, end)]
    total = base + weight * rate
    print(f"{total:.2f}")
else:
    print("Error")
