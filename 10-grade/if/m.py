x, y = map(float, input().split())
area = y > x**2 - 2 and (y < -x or y < x)
print("YES" if area else "NO")
