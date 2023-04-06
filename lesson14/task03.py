def count_element(ls, value):
    count = 0
    index = 0

    while index < len(ls):
        if ls[index] == value:
            count += 1

        index +=1

    return count

def main():
    ls = [1,2,3,4,3,2,1]
    print (count_element(ls,3))
    print(ls.count(3))


main()