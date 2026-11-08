"""3394"""

n, s = map(int, input().split())
forward = [0] + [int(input()) for _ in range(n)]

visited = set()

while s and s not in visited:
    visited.add(s)
    s = forward[s]

print(len(visited))
