def find_perfect_number():
    """
    The function generates the next perfect number.
    :return: A generator of the next perfect number.
    """
    is_perfect_number = 1
    while True:
        (yield is_perfect_number) if sum([number for number in range(1, is_perfect_number)
                                          if is_perfect_number % number == 0]) == is_perfect_number else None
        is_perfect_number += 1


def main():
    perfect_number_generator = find_perfect_number()
    for perfect_number in perfect_number_generator:
        print(perfect_number)


if __name__ == '__main__':
    main()
