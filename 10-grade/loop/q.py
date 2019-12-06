n = int(input())
count = 0

while n**0.5 % 1 != 0:
    n -= 1

print(n)

while n > 1:
    print(n, end=' ')
    n //= 4
    count += 1


if count == 0:
    print(0)
