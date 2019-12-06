num = int(input())

result = True

d_first = num % 10
num //= 10
while num > 0:
    d = num % 10

    if d != d_first:
        result = False
        break

    num //= 10

print("YES" if result else "NO")
