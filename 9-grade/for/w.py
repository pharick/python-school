a = int(input())
b = int(input())
c = int(input())
d = int(input())

a -= c
a += (d - a % d) % d
a += c

for i in range(a, b + 1, d):
    print(i, end=' ')
