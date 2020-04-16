def dec_to_base(n, base):
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
              'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
              'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
              'U', 'V', 'W', 'X', 'Y', 'Z']

    if n < base:
        return digits[n]

    return dec_to_base(n // base, base) + digits[n % base]


def main():
    n, base = map(int, input().split())
    result = dec_to_base(abs(n), base)
    print(result if n >= 0 else '-' + result)


if __name__ == '__main__':
    main()