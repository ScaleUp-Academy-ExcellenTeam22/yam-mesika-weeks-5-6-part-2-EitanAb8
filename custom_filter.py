def custom_filter(function, iterable) -> iter:
    """
    The function filters all values returning true from a given function.
    :param function: A function for the check.
    :param iterable: An iterable object.
    :return: An iter object of the desired value.
    """
    for item in iterable:
        (yield item) if item and function is None else (yield item) if function is not None and function(item) else None


def is_mature(age):
    return age >= 18


def main():
    ages = [0, 1, 4, 10, 20, 35, 56, 84, 120]
    mature_ages = custom_filter(is_mature, ages)
    print(tuple(mature_ages))

    to_sum = [(1, -1), (2, 5), (5, -3, -2), (1, 2, 3)]
    sum_is_not_zero = custom_filter(sum, to_sum)
    print(tuple(sum_is_not_zero))

    to_sum = [0, "", None, 0.0, True, False, "Hello"]
    equivalent_to_true = custom_filter(None, to_sum)
    print(tuple(equivalent_to_true))


if __name__ == '__main__':
    main()
