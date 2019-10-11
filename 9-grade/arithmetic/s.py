roubles = int(input())
kopeks = int(input())
n = int(input())

cost = roubles * 100 + kopeks
sum = cost * n

print(sum // 100, sum % 100)