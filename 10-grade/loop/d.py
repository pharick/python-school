a, b = map(int, input().split())

i = a
while i <= b:
    print('{}*{}={}'.format(i, i, i**2))
    i += 1
