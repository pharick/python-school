a, b = map(int, input().split())
minus = (a < 0) != (b < 0)
a, b = abs(a), abs(b)

i = 0
result = 0
while i < b:
    result += a if not minus else -a
    i += 1

print(result)
