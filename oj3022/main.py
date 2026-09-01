"""changing temperature"""

digits = float(input())
unit = input()
desired = input()
result = 0
if unit != desired:
    if unit == "C" and desired == "F":
        result = digits * 9 / 5 + 32
    elif unit == "C" and desired == "K":
        result = digits + 273.15
    elif unit == "C" and desired == "R":
        result = (digits + 273.15) * 9 / 5
    elif unit == "F" and desired == "C":
        result = (digits - 32) * 5 / 9
    elif unit == "F" and desired == "K":
        result = (digits - 32) * 5 / 9 + 273.15
    elif unit == "F" and desired == "R":
        result = digits + 459.67
    elif unit == "K" and desired == "C":
        result = digits - 273.15
    elif unit == "K" and desired == "F":
        result = (digits - 273.15) * 9 / 5 + 32
    elif unit == "K" and desired == "R":
        result = digits * 9 / 5
    elif unit == "R" and desired == "C":
        result = (digits - 491.67) * 5 / 9
    elif unit == "R" and desired == "F":
        result = digits - 459.67
    elif unit == "R" and desired == "K":
        result = digits * 5 / 9
    print(f"{result:.2f}")
else:
    print(f"{digits:.2f}")
