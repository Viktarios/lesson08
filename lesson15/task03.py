def factorial(number):
    f = 1
    #
    #
    #     while number>1:
    #         f*=number
    #         number -=1
    #
    #     return f

    for item in range(2, number+1):
        f *= item

    return f

print(factorial(5))