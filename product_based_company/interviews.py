# full pyramid and inverted full pyramid

numbers = 5
def full_pyramid(numbers):
    for i in range(1, numbers + 1):
        print(' ' * (numbers - i), end='')
        print('*' * (2 * i - 1))
full_pyramid(numbers)

def inverted_full_pyramid(numbers):
    for i in range(1, numbers + 1):
        spaces = numbers - i
        stars = 2 * i - 1
        print(" " * spaces + "*" * stars)

    for i in range(numbers - 1, 0, -1):
        spaces = numbers - i
        stars = 2 * i - 1
        print(" " * spaces + "*" * stars)
inverted_full_pyramid(numbers)


# half pyramid and inverted half pyramid
numbers = 5
def full_pyramid(numbers):
    for i in range(1, numbers + 1):
        print(' ' * (numbers - i), end='')
        print('*' * (2 * i - 1))

    for i in range(1, numbers + 1):
        print('*' * i)
full_pyramid(numbers)

def inverted_full_pyramid(numbers):
    for i in range(1, numbers + 1):
        spaces = numbers - i
        stars = 2 * i - 1
        print(" " * spaces + "*" * stars)

    for i in range(numbers - 1, 0, -1):
        spaces = numbers - i
        stars = 2 * i - 1
        print(" " * spaces + "*" * stars)
    for i in range(numbers, 0, -1):
        print('*' * i)

inverted_full_pyramid(numbers)


#1 Given two arrays, write a python function to return the intersection of the two? For example, X = [1,5,9,0] and Y = [3,0,2,9] it should return [9,0]

X = [1,5,9,0]
Y = [3,0,2,9]

a = set(X).intersection(set(Y))
print(list(a))

def my_intersection(X,Y):
    result = []
    for i in X:
        if i in Y:
            result.append(i)
    print(result)
my_intersection(X,Y)


#2 Given an array, find all the duplicates in this array? For example: input: [1,2,3,1,3,6,5] output: [1,3]

inp = [1,2,3,1,3,6,5]
outp = [1,3]

def duplicate_values(inp):
    dres = set()
    res = set()
    for i in inp:
        if i in res:
            dres.add(i)
        else:
            res.add(i)
    print(list(dres))
duplicate_values(inp)

