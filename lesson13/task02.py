# 1-10 average
NUMBER_OF_STUDENT = 5


def calc_mark_avg(mark1, mark2, mark3, mark4, mark5):
    sum = mark1
    sum += mark2
    sum += mark3
    sum += mark4
    sum += mark5
    return (mark1 + mark2 + mark3 + mark4 + mark5) / 5


def main():
    mark1 = int(input("Input the mark: "))
    mark2 = int(input("Input the mark: "))
    mark3 = int(input("Input the mark: "))
    mark4 = int(input("Input the mark: "))
    mark5 = int(input("Input the mark: "))
    avg = calc_mark_avg(mark1, mark2, mark3, mark4, mark5)
    avg = round(avg, 1)
    msg = f"Group average mark is {avg}"
    print(msg)


if __name__ == '__main__':
    main()
