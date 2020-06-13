x = int(input())
p = int(input())
y = int(input())

year = 0
while x < y:
    x *= 1 + p / 100
    x = int(x * 100) / 100
    year += 1

print(year)
