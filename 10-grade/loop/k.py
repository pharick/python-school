num = int(input())

count = 0
while num:
    d = num % 10
    
    if d % 2 == 0:
        count += 1

    num //= 10

print(count)
