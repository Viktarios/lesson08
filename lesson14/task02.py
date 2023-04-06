def find_firs_element(ls, value):
    index = 0

    while index < len(ls):
        if ls[index] == value:
            return index

        index += 1

    return None


def find_last_element(ls, value):
    index = len(ls)-1

    while index >= 0:
        if ls[index] == value:
            return index

        index -= 1

    return None