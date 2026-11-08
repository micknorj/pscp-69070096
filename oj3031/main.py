"""ink"""

import math

speed, num_points = map(int, input().split())

for _ in range(num_points):
    x, y = map(int, input().split())

    radius = math.sqrt(x**2 + y**2)
    area = 3.1416 * (radius**2)
    time_needed = area / speed

    print(math.ceil(time_needed))
