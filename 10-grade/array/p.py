from random import randint


def generate_list(a, b, n):
    return [randint(a, b) for i in range(n)]


def mean(arr):
    return sum(arr) / len(arr) if len(arr) != 0 else 0


def main():
    a, b, n = map(int, input().split())
    arr = generate_list(a, b, n)

    less_50 = list(filter(lambda n: n < 50, arr))
    rest = list(filter(lambda n: n >= 50, arr))

    print(*arr)
    print(mean(less_50), mean(rest))


if __name__ == "__main__":
    main()
