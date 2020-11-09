
def sum_up2(end_number):
    sum = 0
    start = 1
    while start <= end_number:
        sum += start
        start += 1

    return sum


# 1, 2, 3, 4, 5

def sum_up3(number):
    if number == 1:
        return 1

    return number + sum_up3(number-1)


# print("sum is %s" % sum_up3(number=10))


# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89
def fib(number):
    if number == 1:
        return 0
    if number == 2:
        return 1

    return fib(number-1) + fib(number-2)

print("11th fib number is ", fib(11))
