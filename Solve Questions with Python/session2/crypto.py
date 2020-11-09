import math
import time

start_time = time.time()


def is_prime(number):
    previous_numbers = range(2, number)
    for p_num in previous_numbers:
        # print(number, "/", p_num, "remainder: ", number % p_num)
        # if p_num > number // 2:     # think the best condition to stop - square root of number
        if p_num > math.sqrt(number):
            break

        if number % p_num == 0:      # p_num is a factor of number
            return False
    return True

#print(is_prime(26391))


def goldbach(number):
    """

    :param number: even number > 2
    :return:
    """
    for number1 in range(2, number//2+1):
        """
        if not is_prime(number1):
            continue
        number2 = number - number1
        if not is_prime(number2):
            continue
        """
        number2 = number - number1
        if is_prime(number1) and is_prime(number2):
            print("The two numbers are ", number1, "and", number2)


def gold_xiaohui(number):
    for i in range(2, number, 1):
        if is_prime(i):
            number1=i
            number2 = number - number1

            if is_prime(number2):
                print(number1, number2)
    # return number1, number2

# gold_xiaohui(10)
goldbach(2000)

# print("15 is prime number", is_prime(15))
# print("29 is prime number", is_prime(29))


end_time = time.time()
print("Used time is ", end_time-start_time, "seconds")
