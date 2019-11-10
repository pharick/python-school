num = int(input())

sum = 0
while num:
    d = num % 10
    sum += d
    num //= 10

print(sum)
