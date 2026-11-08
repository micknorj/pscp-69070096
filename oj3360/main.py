"""3360"""

w, h, _, _ = map(int, input().split())

x = [0] + list(map(int, input().split())) + [w]
y = [0] + list(map(int, input().split())) + [h]

widths = sorted(
    (x[i + 1] - x[i] for i in range(len(x) - 1)),
    reverse=True
)
heights = sorted(
    (y[i + 1] - y[i] for i in range(len(y) - 1)),
    reverse=True
)

first = widths[0] * heights[0]
second = max(widths[1] * heights[0], widths[0] * heights[1])

print(first, second)
