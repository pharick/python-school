a = int(input())
b = int(input())

for i in range(a, b + 1):
    d1 = i % 10
    d2 = i // 10 % 10
    d3 = i % 1000 // 100
    d4 = i // 1000

    if ((d1 == d2 and d1 == d3 and d1 != d4) or
        (d1 == d2 and d1 == d4 and d1 != d3) or
        (d1 == d3 and d1 == d4 and d1 != d2) or
        (d2 == d3 and d2 == d4 and d2 != d1)):
        print(i)
