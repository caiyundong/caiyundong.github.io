"""
for i in range(1, 10):
    print(i, end=" ")

print("")

for i in range(1, 7):
    # for k in range(1, 7-i):
    #     print('\t', end="")
    for j in range(1, 7):
        print(i+j, end="\t")

    print("")





for _row in range(1, 5):
    for _col in range(1, 5):
        print(1, end=" ")
    print("")
"""

for i in range(1, 10):
    for j in range(1, i+1):
        print(i, "x", j, "=", i*j, end="\t")

    print("")
