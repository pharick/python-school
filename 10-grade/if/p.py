x, y = map(float, input().split())

area1 = y > 1 - x and x >= 0 and x < 1
area2 = y > 1 - x and x < 0 and y > 2 * x**2

print("YES" if area1 or area2 else "NO")
