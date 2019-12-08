s = 0
p = 1

k = int(input())

while k != 0:
    s += k
    p *= k
    
    k = int(input())

print(s, p)
