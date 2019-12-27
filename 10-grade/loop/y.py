n = int(input())

l = len(str(n)) - 1

while l >= 0:
    d = 10**l
    print(n // d, end=' ')
    n %= d
    l -= 1
