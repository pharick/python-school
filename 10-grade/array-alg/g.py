def rearrange(arr):
    for i in range(0, len(arr) - 1, 2):
        arr[i], arr[i + 1] = arr[i + 1], arr[i]


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    rearrange(arr)
    print(*arr)


if __name__ == '__main__':
    main()
