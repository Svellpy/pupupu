# #
# numbers_1 = [1, 2, 3, 4, 5]

# average_1 = sum(numbers_1) / len(numbers_1)
# print(average_1)

# #
# numbers_1 = [1, 2, 3, 4, 5]
# numbers_2 = [6, 7, 8, 9, 10]


# def find_average(numbers):
#     average = sum(numbers) / len(numbers)
#     return average


# average_1 = find_average(numbers_1)
# average_2 = find_average(numbers_2)
# print(average_1, average_2) 

# #
# def count_vowels(string):
#     VOWELS = "aeiouAEIOU"
#     count = 0
#     for char in string:
#         if char in VOWELS:
#             count +=1
#     return count

# print(count_vowels("Hello, world!"))

# #
# def nothing():
#     pass

# #

# def format_date(*, day: int, month: str)-> str:
#     return f"The date is {day} of {month}"


# print(format_date(month="May", day=15))


#
def customer_greeting(*, name: str, greeting: str = "Hello") -> str:
    return f"{greeting}, {name}"

print(customer_greeting(name = "Sveta", greeting="Good morning"))
print(customer_greeting(name="Sveta"))