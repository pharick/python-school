a, b = map(int, input().split())
count = 0

for i in range(a, b + 1):
    simple = True

    for d in range(2, i // 2 + 1):
        if i % d == 0:
            simple = False
            break

    if simple:
        print(i, end=' ')
        count += 1

if count == 0:
    print(0)