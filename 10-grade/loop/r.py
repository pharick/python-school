a, b = map(int, input().split())
i = 0

while a != 0:
    if b > a:
        a, b = b, a
    
    a -= b
    i += 1

print(b, i)
