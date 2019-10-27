from random import randint

a, b, n = map(int, input().split())

i = 1
while i <= n:
    print(randint(a, b), end=' ')
    i += 1
print()
