x, y = map(float, input().split())

area1 = x**2 + y**2 < 1
area2 = x > 0 and y > 0 and x < 1 and y < 1

print("YES" if area1 or area2 else "NO")
