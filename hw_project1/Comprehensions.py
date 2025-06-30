# #
# squares = []
# for x in range(10):
#     squares.append(x ** 2)

#     print(squares)

# #
# squars = [x ** 2 for x in range(10)]

# print(squars)

# #
# even_squares = []
# for x in range(10):
#     if x % 2 == 0:
#         even_squares.append(x ** 2)

#     print(even_squares)

##
# even_squares = [x ** 2 for x in range(10) if x % 2 == 0]

# print(even_squares)

# #
# labbeled_numbers = []
# numbers = [1, 2, 3, 4, 5]

# for num in numbers:
#     if num % 2 == 0:
#         labbeled_numbers.append("even")
#     else:
#         labbeled_numbers.append("add")

#         print(labbeled_numbers)

# ##
# numbers = [1, 2, 3, 4, 5]
# labbeled_numbers = ["even" if num % 2 == 0 else "add" for num in numbers]

# print(labbeled_numbers)



# #
# square_dict = {x: x ** 2 for x in range(10)}

# print(square_dict)

# #
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# transpose_matrix = []
# for i in range(len(matrix)):
#     transpose_row = []
#     for row in matrix:
#         transpose_row.append(row[i])
#     transpose_matrix.append(transpose_row)

# print(transpose_matrix)

##
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transpose_matrix = [[row[i] for row in matrix] for i in range(len(matrix))]

print(transpose_matrix)