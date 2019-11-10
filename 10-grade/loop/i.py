a, b = map(int, input().split())

count = 0
i = a
while i <= b:
    d_count = len(str(i))
    d_sum = 0
    num = i
    while num:
        d = num % 10
        d_sum += d**d_count
        num //= 10

    if d_sum == i:
        print(i, end=' ')
        count += 1

    i += 1

if not count:
    print(-1)
