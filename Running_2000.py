import time


def timer(f, *args, **kwargs):
    """
    The function calculates the running time of a given function.
    :param f: A given function.
    :param args: Non Keyword Arguments.
    :param kwargs: Keyword Arguments.
    :return: The execution time of the given function.
    """
    start_time = time.time()
    map(f, (args, kwargs))
    return start_time - time.time()


def main():
    print(timer(print, "Hello"))
    print(timer(zip, [1, 2, 3], [4, 5, 6]))
    print(timer("Hi {name}".format, name="Bug"))


if __name__ == '__main__':
    main()
