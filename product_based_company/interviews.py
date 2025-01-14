numbers = 5
def half_pyramid(numbers):
    for i in range(1, numbers + 1):
        print(' ' * (numbers - i), end='')
        print('*' * (2 * i - 1))

half_pyramid(numbers)


def my_pyramid(numbers):
    for i in range(1, numbers + 1):
        spaces = numbers - i
        stars = 2 * i - 1
        print(" " * spaces + "*" * stars)

    for i in range(numbers - 1, 0, -1):
        spaces = numbers - i
        stars = 2 * i - 1
        print(" " * spaces + "*" * stars)

my_pyramid(numbers)


