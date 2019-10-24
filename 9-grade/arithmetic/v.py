n = int(input())
k = int(input())

more_than_other = k % n
less_than_other = n - more_than_other

print(less_than_other % n)
