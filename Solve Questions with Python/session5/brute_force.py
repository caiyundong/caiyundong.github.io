import random
lock_code = random.randint(1000, 9999)

# print(lock_code)


def check_the_lock(_lock_code):
    for key1 in range(0, 10):
        for key2 in range(0, 10):
            for key3 in range(0, 10):
                for key4 in range(0, 10):
                    my_guess = key1*1000+key2*100+key3*10+key4
                    # print(my_guess, _lock_code)

                    # if my_guess == _lock_code:
                    if key1+key2+key3+key4 == 19 and key1 == key4*4 and key2 == key3*2:
                        print("I find the key:", my_guess)
                        return

    print("Failed to find the key")

check_the_lock(lock_code)
