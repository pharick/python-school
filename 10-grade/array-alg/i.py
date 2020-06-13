def reverse(arr):
    for i in range(len(arr) // 2):
        arr[i], arr[-i - 1] = arr[-i - 1], arr[i]


def main():
    input()
    arr = list(map(int, input().split()))
    reverse(arr)
    print(*arr)


if __name__ == '__main__':
    main()
