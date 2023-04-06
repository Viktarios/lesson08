# 1234567

def check_all_even_digits(number):
    while number > 0:
        digit = number % 10
        if digit % 2 == 1:
            return False
        number //= 10

    return True


print(check_all_even_digits(1888888))
