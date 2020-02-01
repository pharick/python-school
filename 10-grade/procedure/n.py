def nega_two(number):
    result = ''

    while number != 0:
        d = number % -2
        number = number // -2

        if (d < 0):
            d += 2
            number += 1

        result = str(d) + result

    return int(result)


def main():
    number = int(input())
    print(nega_two(number))


if __name__ == '__main__':
    main()
