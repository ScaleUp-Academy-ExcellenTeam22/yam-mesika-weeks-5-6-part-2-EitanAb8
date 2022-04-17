import re
""" I have used help from this site to solve this task:
https://www.geeksforgeeks.org/python-extract-words-from-given-string/"""


def count_words(text) -> dict:
    """
    The function creates and returns a dictionary of words and their len.
    :param text: A string.
    :return: A dictionary of words and their len.
    """
    return {word: len(word) for word in re.findall(r'\w+', text)}


def main():
    text = """
    You see, wire telegraph is a kind of a very, very long cat.
    You pull his tail in New York and his head is meowing in Los Angeles.
    Do you understand this?
    And radio operates exactly the same way: you send signals here, they receive them there.
    The only difference is that there is no cat.
    """
    print(count_words(text))


if __name__ == '__main__':
    main()
