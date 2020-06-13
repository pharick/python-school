def longest_sequence(arr):
    result_n = arr[0]
    result_l = 0

    current = arr[0]
    l = 0

    for n in arr:
        if n == current:
            l += 1
        else:
            if l > result_l:
                result_n = current
                result_l = l

            l = 1
            current = n

    if l > result_l:
        result_n = current
        result_l = l

    return result_n, result_l


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    print(*longest_sequence(arr))


if __name__ == '__main__':
    main()
