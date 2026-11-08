"""3355"""

nums = []

while True:
    n = int(input())
    if n == -1:
        break
    nums.append(n)

result = []

if nums:
    start = end = nums[0]

    for n in nums[1:]:
        if n == end + 1:
            end = n
        else:
            result.append(str(start) if start == end else f"{start}-{end}")
            start = end = n

    result.append(str(start) if start == end else f"{start}-{end}")

print(", ".join(result))
