def words_length(sentence) -> iter:
    """
    The function returns the len of every word in a string.
    :param sentence: A string.
    :return: An iter object of the len of the words in the sentence.
    """
    return (len(word) for word in sentence.split(' '))


def main():
    sentence = "Toto, I've a feeling we're not in Kansas anymore"
    print(list(words_length(sentence)))


if __name__ == '__main__':
    main()
