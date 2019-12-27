n = int(input())

a = 1
b = 1

for i in range(n):
    print(a, end=' ')
    new = a + b
    a = b
    b = new
