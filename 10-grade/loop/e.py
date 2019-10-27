a, b = map(int, input().split())

sum = 0
i = a
while i <= b:
    sum += i**2
    i += 1

print(sum)
