def get_positive_numbers() -> list:
    """
    The function finds all positive numbers in an input.
    :return: A list of the positive numbers found in the user's input.
    """
    return list(filter(lambda number: number >= 0, [int(number) for number in input().split(',')]))


def main():
    print(get_positive_numbers())


if __name__ == '__main__':
    main()
