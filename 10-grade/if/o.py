x, y = map(float, input().split())
area = x**2 + y**2 < 1 and (y < x or y > -x)
print("YES" if area else "NO")
