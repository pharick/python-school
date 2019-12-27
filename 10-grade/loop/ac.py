from math import sqrt

n = int(input())
count = 0

for i in range(6, n + 1):
    s = 1
    for j in range(2, int(sqrt(i)) + 1):
        if i % j == 0:
            s += j + i // j
        if s > i:
            break

    if s == i:
        print(i, end=' ')
        count += 1

if count == 0:
    print(0)
