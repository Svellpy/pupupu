# #
# fruits = ["banana", "apple", "cherry", "date"]
# #sorted_fruits = sorted(fruits)
# sorted_fruits = sorted(fruits, reverse=True)

# print(sorted_fruits)

# #
# fruits = ["banana", "apple", "cherry", "date"]

# def sort_by_len(element: str) -> int:
#     return len(element)

# sorted_fruits = sorted(fruits, key=sort_by_len)

# print(sorted_fruits)

# # print(sort_by_len)
# # print(type(sort_by_len))

# #
# people = [
#     {"name": "Alice", "age": 25},
#     {"name": "Bob", "age": 20},
#     {"name": "Charlie", "age": 30},
# ]

# # def sort_by_age(person: dict) -> int:
# #     return person["age"]

# # sorted_people = sorted(people, key=sort_by_age)

# # print(sorted_people)

# def sort_by_age_name(element: dict) -> tuple[int, str]:
#     return element["age"], element["name"]

# sorted_people = sorted(people, key=sort_by_age_name)

# print(sorted_people)