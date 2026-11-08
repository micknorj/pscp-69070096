"""3357"""

n = int(input())
heights = [int(input()) for _ in range(n)]
heights = [0] + heights + [0]

count = 0

for i in range(1, n + 1):
    if heights[i] > heights[i - 1] and heights[i] > heights[i + 1]:
        count += 1

print(count)
