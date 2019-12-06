n = int(input())

if n % 2 != 0:
    n -= 1

count = 0

for i in range(n, 1, -2):
    print(2**i, end=' ')
    count += 1

if count == 0:
    print(0)
