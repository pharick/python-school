a, b = map(int, input().split())

i = a
while i <= b:
    is_divisible = True
    
    num = i
    while num > 0:
        d = num % 10

        if d == 0 or i % d != 0:
            is_divisible = False
            break

        num //= 10

    if is_divisible:
        print(i, end=' ')

    i += 1

print()
