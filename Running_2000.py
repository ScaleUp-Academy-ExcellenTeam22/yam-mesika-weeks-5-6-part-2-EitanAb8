import timeit


def timer(f, *args, **kwargs):
    """
    The function calculates the running time of a given function.
    :param f: A given function.
    :param args: Non Keyword Arguments.
    :param kwargs: Keyword Arguments.
    :return: The execution time of the given function.
    """
    return timeit.Timer(lambda: map(f, args, kwargs)).timeit()


def main():
    print(timer(print, "Hello"))
    print(timer(zip, [1, 2, 3], [4, 5, 6]))
    print(timer("Hi {name}".format, name="Bug"))


if __name__ == '__main__':
    main()
