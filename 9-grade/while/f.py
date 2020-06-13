x = int(input())
y = int(input())

day = 1
while x < y:
    x *= 1.10
    day += 1

print(day)