"""3299"""

l, n = (int(x) for x in input().split())

band = 1

while (band * l) * (band * l + 1) // 2 < n:
    band += 1

print(band)
