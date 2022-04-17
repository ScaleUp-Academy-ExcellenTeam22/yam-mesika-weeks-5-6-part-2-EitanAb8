def full_names(first_names_list, last_names_list, min_length=0) -> list:
    """
    The function creates a list of first and last names out of 2 lists, in term they are long than the min len.
    :param first_names_list: A list of first names.
    :param last_names_list: A list of last names.
    :param min_length: An integer of min full name length.
    :return: A new list of full names (with capital letters).
    """
    return [first_name.capitalize()+' '+last_name.capitalize()
            for first_name in first_names_list for last_name in last_names_list
            if len(first_name+' '+last_name) >= min_length]


def main():
    first_names = ['avi', 'moshe', 'yaakov']
    last_names = ['cohen', 'levi', 'mizrahi']

    print(full_names(first_names, last_names, 10))
    print(full_names(first_names, last_names))


if __name__ == '__main__':
    main()
