num = int(input())

result = False

d_prev = num % 10
num //= 10
while num > 0:
    d = num % 10

    if d_prev == d:
        result = True
        break

    d_prev = d
    num //= 10

print("YES" if result else "NO")
