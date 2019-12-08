k = int(input())
min = k
max = k

while k != 0:
    if k < min:
        min = k
    if k > max:
        max = k

    k = int(input())

print(min, max)
