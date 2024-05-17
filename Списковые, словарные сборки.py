numbers = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]

odd_squares = list(filter(lambda x: x % 2 != 0, map(lambda x: x**2, numbers)))

print(odd_squares)



