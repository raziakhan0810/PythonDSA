"""
Q) Find missing number from a Array [3,1,3]
"""
def find_missing_number(lst):
    n = len(lst)
    total_sum = n * (n + 1) // 2
    actual_sum = sum(lst)
    square_sum = sum(x * x for x in lst)
    expected_square_sum = sum(i * i for i in range(1, n + 1))

    sum_diff = total_sum - actual_sum
    square_diff = expected_square_sum - square_sum

    missing = (sum_diff + (square_diff // sum_diff)) // 2
    repeating = missing - sum_diff

    print(f"Missing = {missing}, Repeating = {repeating}")

lst = [3, 1, 3]
find_missing_number(lst)
