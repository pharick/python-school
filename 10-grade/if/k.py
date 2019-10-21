from math import sin, pi

x, y = map(float, input().split())
area = y < sin(x) and y > 0 and y < 0.5 and x > 0 and x < 2 * pi

print("YES" if area else "NO")