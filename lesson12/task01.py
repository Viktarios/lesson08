from random import randrange

SIDE_COIN = 2


def throw_coin(count):
    if count <= 0:
        return 0, 0

    heads = 0
    counter = 0

    if count > 0:
        while counter < count:

            side = randrange(SIDE_COIN)

            if side == 0:
                heads += 1

            counter += 1

    return heads, counter - heads


def main():
    count = int(input("Input count of throwing: "))
    heads, tails = throw_coin(count)

    msg = f"Count of heads is {heads}, count of tails is {tails}"
    print(msg)


def tet_heads():
    count = 10
    heads, tails = throw_coin(count)
    return heads > 0


def test_tails():
    count = 10
    heads, tails = throw_coin(count)
    return tails > 0


def test_invalid_data():
    count = -5
    heads, tails = throw_coin(count)
    return heads == 0 and tails == 0


def test_suite():
    msg = "test_heads - " + str(tet_heads())
    msg += "\ntest_tails - " + str(test_tails())
    msg += "\ntest_invalid_data - " + str(test_invalid_data())

    print(msg)

test_suite()
