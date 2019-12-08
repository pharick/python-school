from math import log2, trunc

n = int(input())
count = 0

s = trunc(log2(n))

if s % 2 != 0:
    s -= 1

for i in range(s, 1, -2):
    print(2**i, end=' ')
    count += 1

if count == 0:
    print(0)
