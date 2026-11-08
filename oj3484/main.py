"""3484"""

n, p = input().split()
n = int(n)
p = float(p)

tiles = [list(map(int, input().split())) for _ in range(n)]

total_tiles = 0
total_points = 0

for row in tiles:
    count = sum(x > 0 for x in row)
    points = sum(row)
    total_tiles += count
    total_points += points
    print(*row, count, points)

print(*(sum(tiles[i][j] > 0 for i in range(n)) for j in range(n)))
print(*(sum(tiles[i][j] for i in range(n)) for j in range(n)))
print(total_tiles, total_points, f"{total_points * p:.2f}")
