from math import sqrt


def get_quarter(x, y):
    if x > 0 and y > 0:
        return 1
    if x < 0 and y > 0:
        return 2
    if x < 0 and y < 0:
        return 3
    if x > 0 and y < 0:
        return 4
    return 0


def get_max_quarter(quarters):
    result = 1
    count = len(quarters[1])
    
    for i in range(2, 5):
        if len(quarters[i]) > count:
            result = i
            count = len(quarters[i])

    return result


def get_dist_to_axis(point):
    x, y = point
    return min(abs(x), abs(y))


def get_closest_to_axis(points):
    result = points[0]
    dist = get_dist_to_axis(points[0])

    for i in range(1, len(points)):
        if get_dist_to_axis(points[i]) < dist:
            dist = get_dist_to_axis(points[i])
            result = points[i]

    return result
    

n = int(input())
quarters = {1: [], 2: [], 3: [], 4: []}

for i in range(n):
    x, y = map(int, input().split())
    quarter = get_quarter(x, y)
    
    if quarter != 0:
        quarters[quarter].append((x, y))

max_quarter = get_max_quarter(quarters)
closest = get_closest_to_axis(quarters[max_quarter])
dist = min(abs(closest[0]), abs(closest[1]))

print('K =', max_quarter)
print('M =', len(quarters[max_quarter]))
print('A =', closest)
print('R =', dist)