a = int(input())
b = int(input())
c = int(input())

if b > a:
    a, b = b, a
if c > a:
    a, c = c, a

if b + c <= a:
    print('impossible')
elif b**2 + c**2 < a**2:
    print('obtuse')
elif b**2 + c**2 > a**2:
    print('acute')
else:
    print('rectangular')
