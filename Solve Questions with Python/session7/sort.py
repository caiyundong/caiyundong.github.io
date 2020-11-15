import random


def bubble_sort1(l):
    print(l)
    if l and len(l) == 0:
        return l

    # [1, 2, 3, 4, 5]
    for index1, number1 in enumerate(l):
        for index2, number2 in enumerate(l):
            if number1 > number2:
                l[index1], l[index2] = l[index2], l[index1]
        print("--", l)
    print(l)


def bubble_sort2(l):
    print("original list:", l)
    if l and len(l) == 0:
        return l

    num = len(l)
    i = 0
    while i < num:
        k = i
        j = k + 1
        while j < num:
            if l[i] > l[j]:
                l[i], l[j] = l[j], l[i]
                print(i, j, l)
            j += 1
            k += 1
        i += 1
        print("========", l)
    print("final list:", l)


def insert_ort(l):
    print(l)
    sorted_l = []

    for i in l:
        # insert i into sorted_l
        if len(sorted_l) == 0:
            sorted_l.append(i)
        else:
            last_index = 0
            for index, j in enumerate(sorted_l):
                last_index = index
                if i < j:
                    break

            sorted_l.insert(last_index, i)

    print(sorted_l)


def merge_sort(l): #[2,4, 5,1, 7,9,3,10]
    print(l)
    _len = len(l)
    if _len == 1:
        return l
    elif _len == 2:
        if l[0] <= l[1]:
            return l
        else:
            l[0], l[1] = l[1], l[0]
            return l
    else:
        result1 = merge_sort(l[0:_len//2])  # [2,4,5,1] -> []
        result2 = merge_sort(l[_len//2:])   # [7,9,3,10] -> [7, 9, 10]
                                            # [1, 2, 3,  4, 5, 7, 9, 10]
        print(result1, result2)
        result = []
        # combine the two lists
        while len(result1) > 0 or len(result2) > 0:
            print(result1, result2)
            if len(result1) == 0:
                result += result2
                result2 = []
            elif len(result2) == 0:
                result += result1
                result1 = []
            else:
                if result1[0] < result2[0]:
                    result.append(result1[0])
                    result1 = result1[1:]
                else:
                    result.append(result2[0])
                    result2 = result2[1:]
        print(result)
        return result


l = list(range(1, 9))
random.shuffle(l)
# bubble_sort2(l)
# insert_ort(l)
merge_sort(l)
