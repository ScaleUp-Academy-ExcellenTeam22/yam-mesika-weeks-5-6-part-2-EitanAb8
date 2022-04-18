def interleave(*iterables) -> iter:
    """
    The function generates a generator of intertwined values of the iterable arguments.
    :param iterables: list of iterables arguments.
    :return: a generator of intertwined values.
    """
    return (iterables[place][item] for item in range(len(iterables)) for place in range(len(iterables)))


def main():
    print(list(interleave('abc', [1, 2, 3], ('!', '@', '#'))))


if __name__ == '__main__':
    main()
