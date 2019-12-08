n = int(input())
s = 0
p = 1

for i in range(n):
    k = int(input())
    s += k
    p *= k

print(s, p)
