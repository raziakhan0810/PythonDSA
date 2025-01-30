# print out fib sequence - output - 0112358
n =  7
a, b = 0, 1
fib_sequence = ""
for _ in range(n):
    fib_sequence += str(a)
    a, b = b, a + b
print(fib_sequence)


# print out the count of char - output - a2n2d1i2
str1 = 'indiana'
result = ''
for char in set(str1):
    result += char + str(str1.count(char))
print(result)