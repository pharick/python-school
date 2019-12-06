num = int(input())

result = False

while num > 0:
    d = num % 10
    num //= 10

    num2 = num
    while num2 > 0:
        d2 = num2 % 10
        num2 //= 10

        if d == d2:
            result = True
            break

    if result:
        break

print("YES" if result else "NO")
