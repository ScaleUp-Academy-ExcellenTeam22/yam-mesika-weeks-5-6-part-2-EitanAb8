from collections import defaultdict

"""
In order to solve this exercise i learned from the following topic at "stackoverflow":
https://stackoverflow.com/questions/36549449/dictionary-comprehension-for-list-values
"""


def group_by(function, iterable: iter) -> dict:
    """
    The function returns a dictionary of keys from function and values from iterable
    related to the function's return.
    :param function: A function.
    :param iterable: An iterable structure.
    :return: A dictionary of keys and values related to the keys returned from the function.
    """
    group = defaultdict(list)
    for element in iterable:
        group[function(element)].append(element)
    return dict(group)


def main():
    print(group_by(len, ["hi", "bye", "yo", "try"]))


if __name__ == '__main__':
    main()
