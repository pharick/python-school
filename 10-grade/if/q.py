x, y = map(float, input().split())

area1 = y < 1 and x > 0 and y > x - 1
area2 = x > 0 and x**2 + y**2 < 1

print("YES" if area1 or area2 else "NO")
