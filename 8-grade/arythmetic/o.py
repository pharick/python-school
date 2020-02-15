n = int(input())
n %= 86400

s = n % 60
m = n // 60
h = m // 60
m %= 60

print(h, ":",
      m // 10, m % 10, ":",
      s // 10, s % 10,
      sep="")