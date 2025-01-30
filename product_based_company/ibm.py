"""
Q1) Find the next highest value of a number in a list? L = [20, 4, 10, 60, 1, 4, 8]
Input: 4 Output: 8
"""

import bisect
lst = [20, 4, 10, 60, 1, 4, 8]
num = 4

def nest_highest_value(lst, num):
    lst = sorted(set(lst))
    index = bisect.bisect_right(lst, num)
    if index < len(lst):
        return lst[index]
    return None
print(nest_highest_value(lst, num))

def next_highest(lst):
    lst_sorted = sorted(set(lst))
    index = lst_sorted.index(4)
    next_highest = lst_sorted[index + 1]
    return next_highest
print(next_highest(lst))


"""
Q2) generate odd number between 1-10
"""

odd_num = list(range(1, 11, 2))
print(odd_num)

odd_num_lst = [x for x in range(10) if x % 2 != 0]
print(odd_num_lst)

odd_lst = []
for x in range(10):
    if x % 2 != 0:
        odd_lst.append(x)
print(odd_lst)


