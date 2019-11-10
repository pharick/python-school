a, b = map(int, input().split())

count = 0
i = a
while i <= b:
    d_count = len(str(i))

    if (i**2) % (10**d_count) == i:
        print(i, end=' ')
        count += 1

    i += 1

if not count:
    print(-1)
