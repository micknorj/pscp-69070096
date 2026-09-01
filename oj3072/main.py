"""vowels checker"""

word = input().lower()
count = 0
va, ve, vi, vo, vu = 0, 0, 0, 0, 0
for i in range(0, len(word)):
    if word[count] == "a":
        va += 1
    if word[count] == "e":
        ve += 1
    if word[count] == "i":
        vi += 1
    if word[count] == "o":
        vo += 1
    if word[count] == "u":
        vu += 1
    count += 1
    i += 1
if va > 0:
    print(f"a : {va}")
if ve > 0:
    print(f"e : {ve}")
if vi > 0:
    print(f"i : {vi}")
if vo > 0:
    print(f"o : {vo}")
if vu > 0:
    print(f"u : {vu}")
