from math import sqrt

n = int(input())
s = 1
divs = []

for i in range(2, int(sqrt(n)) + 1):
    if n % i == 0:
        divs.append(i)
        divs.append(n // i)
        s += i + n // i

if s == n:
    print(1, *sorted(divs))
else:
    print(0)