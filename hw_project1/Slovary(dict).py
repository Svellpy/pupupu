# person = {
#     "name": "Sveta",
#     "age": 22,
#     "city": "Samara"
# }

# person["job"] = "Nurse"

# print(person)

# #
# person = {}

# person["name"] = "Sveta"
# person["age"] = 22
# person["city"] = "Samara"

# print(person)

# #

# person = {
#     "name": "Sveta",
#     "age": 22,
#     "city": "Samara"
# }

# print(person.get("country", "USA"))
# print(person.get("name", "Grisha"))


#

# person = {
#     "name": "Sveta",
#     "age": 22,
#     "city": "Samara"
# }

# for kay, value in person.item:
#     print(kay)
#     print(value)


#
person = {
    "name": "Sveta",
    "age": 22,
    "city": "Samara"
}
additional_person_info = {
    "job": "Nurse",
    "married": True,
    "city": "Kanava"
}
#person.update(additional_person_info)
person = person | additional_person_info
print(person)