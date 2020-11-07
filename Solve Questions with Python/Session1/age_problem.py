birth_year = int(input("What is your birth year > "))

print("Birth year is ", birth_year)

age = 2020 - birth_year

if age < 7:
    print("You are a kid")
elif 7 <= age < 20:
    print("You are a student")
else:
    print("You need to grab a job")

