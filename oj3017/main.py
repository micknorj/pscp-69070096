"""bill"""

price = int(input())
service = price * 0.1
if service < 50:
    service = 50
elif service >= 1000:
    service = 1000
vat = (price + service) * 0.07
net = price + service + vat
print(f"{net:.2f}")
