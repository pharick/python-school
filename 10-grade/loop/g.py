a, b = map(int, input().split())
c, d = map(int, input().split())

count = 0

i = 10000
while i <= 99999:
    if i % a == b and i % c == d:
        print(i, end=' ')
        count += 1

    i += 1

if count == 0:
    print(-1)

print()
