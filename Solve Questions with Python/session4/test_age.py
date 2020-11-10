age = 5

if age < 7:
    print("age is less than 7")
else:
    print("age is greater than 7")

"""
def wake_up():
    print("wake up")

def have_breakfast():
    print("have breakfast")

b_not_sunday = True
while b_not_sunday:
    wake_up()
    have_breakfast()

numbers = [1, 3, 4, 8, 11, 36, 100]

sum = 0
for a_number in numbers:
    sum = sum + a_number

print("The sum of the list is ", sum)

"""

# a > b, a = 12, b = 8
def gcd(a, b):
    _gcd = 1
    for factor in range(1, b+1):
        if a % factor == 0 and b % factor == 0:
            _gcd = factor

    return _gcd


def gcd2(a, b):     # a > b
    pass


print(gcd2(12, 8))           # 4
print(gcd2(75, 50))          # 25
