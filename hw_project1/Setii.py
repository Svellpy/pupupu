# #
# my_set = {1, 2, 3, 4, 5}

# print(type(my_set))
# print(my_set)


# #
# my_set = set()

# for i in range(5):
#     my_set.add(i)

# print(my_set)


# #
# my_set = {0, 1, 2, 3, 4}

# my_set.remove(2)

# print(my_set)

# #
# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}

# print(set1.union(set2))

# #
# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}

# united_set = (set1.union(set2))

# print(len(united_set))

# #
# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}

# print(set1. intersection(set2))

# #
# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}

# print(set1.difference(set2))

# #
# squares = {x ** 2 for x in range(10)}

# print(squares)

# #
# numbers = [1, 2, 2, 3, 4, 4, 5, 6 ,6 ,7]

# unique_numbers = set(numbers)

# print(type(unique_numbers))
# print(unique_numbers)

#
numbers = [1, 2, 2, 3, 4, 4, 5, 6 ,6 ,7]
unique_numbers = list(set(numbers))

print(unique_numbers)
print(type(unique_numbers))

