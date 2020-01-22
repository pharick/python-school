n = int(input())
data = [int(input()) for i in range(n)]
minProd = 1000

for i in range(n):
    for j in range(i + 6, n):
        prod = data[i] * data[j]
        if prod % 2 != 0 and prod < minProd:
            minProd = prod

print(-1 if minProd == 1000 else minProd)
