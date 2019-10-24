number = int(input())

half1 = number // 100
half2 = number % 100

half2 = half2 % 10 * 10 + half2 // 10

print(half1 - half2 + 1)
