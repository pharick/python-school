n = int(input())

tickets60 = n // 60
n %= 60

tickets10 = n // 10
n %= 10

tickets1 = n

if tickets1 * 15 > 125:
    tickets1 = 0
    tickets10 += 1

if tickets1 * 15 + tickets10 * 125 > 440:
    tickets1 = 0
    tickets10 = 0
    tickets60 += 1

print(tickets1, tickets10, tickets60)
