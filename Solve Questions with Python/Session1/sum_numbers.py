numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# numbers = list(range(1,11))


def sum_up(numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum


# sum up from 1 to 100
def sum_up2(numbers):
    sum = 0
    start = 1
    while start < 100:
        sum += start
        start += 1

    return sum

print("sum is %s" % sum_up2(numbers=numbers))
