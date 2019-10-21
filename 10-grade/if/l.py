x, y = map(float, input().split())

area1 = y < 2 - x**2 and y > x
area2 = y < 2 - x**2 and y > 0

print("YES" if area1 or area2 else "NO")