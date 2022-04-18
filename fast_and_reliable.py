import timeit


def average_runtime(iterable, word):
    """
    The function calculates the average time to find a word in a data structure.
    :param iterable: An iterable data structure.
    :param word: A string.
    :return: The time took to find the word in the data structure.
    """
    return timeit.Timer(lambda: word in iterable).timeit(number=1000)


def main():
    words_file = open("words.txt", "r")
    words_list = list(words_file.read().split('\n'))
    words_set = set(words_list)

    print(average_runtime(words_list, "zwitterion"))
    print(average_runtime(words_set, "zwitterion"))


if __name__ == '__main__':
    main()
