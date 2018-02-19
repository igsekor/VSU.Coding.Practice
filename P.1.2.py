# i = 0
# a = 4
# b = 6
#
# c = 0

# l = []
#
# while i < 50:
#     if i == 1:
#         c = a * b - i
#     elif i > 9:
#         c = a * i
#     elif i < 10:
#         c = i
#     else:
#         c = 0
#     l.append(c)
#     i = i + 1
#
# print(l[43])

small_group_persons_count = 9
cake_count_for_one_person = 3
cake_count_for_small_group = 3.5
cake_count_for_big_group = 3.3

def isEven(number):
    if number % 2 == 0:
        return True
    else:
        return False

def calcCakeCountForEven(personsCount):
    return personsCount * cake_count_for_small_group

def calcCakeCountForOdd(personsCount):
    return personsCount * cake_count_for_small_group + 0.5

def calcCakeCountForSmallGroup(personsCount):
    if isEven(personsCount):
        return calcCakeCountForEven(personsCount)
    else:
        return calcCakeCountForOdd(personsCount)

def calcCakeCount(personsCount):
    if personsCount < 1:
        return 0
    elif personsCount == 1:
        return cake_count_for_one_person
    elif personsCount < small_group_persons_count:
        return calcCakeCountForSmallGroup(personsCount)
    else:
        return int(personsCount * cake_count_for_big_group)

print(calcCakeCount(8))