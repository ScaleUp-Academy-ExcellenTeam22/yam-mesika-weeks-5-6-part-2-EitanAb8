def get_letters() -> list:
    """
    The function creates an array of a-z and A-Z.
    :return: an array of letters.
    """
    return [chr(letter) for letter in range(ord('a'), ord('z') + 1)] + \
           [chr(letter) for letter in range(ord('A'), ord('Z') + 1)]


def main():
    print(get_letters())


if __name__ == '__main__':
    main()
