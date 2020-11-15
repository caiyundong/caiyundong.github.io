import random

def random_examples():
    print(random.random())
    print(random.randint(1, 6))     # random number from 1 to 6
    print(random.choices([1, 2, 3, 4, 6]))

    cards = []
    # spade, heart, diamond, club
    for category in ['♠', '♡', '♢', '♣']:
        for number in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']:
            card = category + number
            cards.append(card)

    print(cards)
    random.shuffle(cards)
    print(cards)


# random_examples()


def roll_two_dice():
    first_dice = random.randint(1, 6)
    second_dice = random.randint(1, 6)

    return first_dice+second_dice


def test_two_dice():
    count = {}
    for i in range(2, 13):  # sum of two dices is from 2 to 12
        count[i] = 0
    print(count)

    for i in range(1, 100000):        # do a simulation
        current_roll = roll_two_dice()
        count[current_roll] += 1

    # print out the result
    for k, v in count.items():
        print("sum - ", k, " Count -", v)


# test_two_dice()

"""
for i in range(1, 7):
    for j in range(1, 7):
        print(i+j, end="\t")

    print("")
"""

def calculate_pi():
    count_circle = 0
    total_number = 5000000
    for i in range(1, total_number):
        x = random.random()
        y = random.random()
        if (x-0.5)*(x-0.5) + (y-0.5) * (y-0.5) < 0.5 * 0.5:
            count_circle += 1

    print(count_circle*4/total_number)

calculate_pi()

