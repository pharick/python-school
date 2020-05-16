from random import randint


def generate_list(a, b, n):
    return [randint(a, b) for i in range(n)]


def mean(arr):
    return sum(arr) / len(arr)


def main():
    a, b, n = map(int, input().split())
    arr = generate_list(a, b, n)
    print(*arr)
    print(mean(arr))


if __name__ == "__main__":
    main()
