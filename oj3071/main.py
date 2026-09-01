"""number in range [A,B] that leaves r remainder when divided by d"""

digit_A = int(input())
digit_B = int(input())
divisor = int(input())
remainder = int(input())
count = 0
if digit_A < digit_B:
    for i in range(digit_A, digit_B + 1):
        if i % divisor == remainder:
            count += 1
        i += 1
    print (count)
