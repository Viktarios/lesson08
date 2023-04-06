a = 10
def test1():
    global a
    a=20
    print(a)


def test2():
    print(a)

test1()
test2()