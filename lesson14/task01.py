def find_element(ls, value):
    index = 0

    while index < len(ls):
        if ls[index] == value:
            return True

        index += 1

    return False
