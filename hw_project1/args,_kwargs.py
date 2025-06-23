# def add_all(*args):
#     summary = 0
#     for num in args:
#         summary += num
#     return summary

# print(add_all(1, 2, 3))

# values = [1, 2, 3, 4, 5]
# other_values = [6, 7, 8, 9, 10]

# print(add_all(*values, *other_values))

# #

# def introduce(**kwargs):
#     print(kwargs)
#     print(type(kwargs))

# introduce(name="Sveta", age=22, city="Samara")


# #

# def func_with_all_arguments(x:int, y: int, *args, value: int = 6, **kwargs):
#     print(x, y)
#     print(args)
#     print(value)
#     print(kwargs)

# person = {
#     "name": "Sveta",
#     "age": 22,
#     "city": "Samara"
# }

# func_with_all_arguments(1, 2, 3, 4, 5, **person)

#

def modify_dict(old_dict: dict, **kwargs) -> tuple[dict, bool]:
    is_modify = False

    for kay, value in kwargs.items():
        if old_dict.get(kay) != value:
            old_dict[kay] = value
            is_modify = True

        return old_dict, is_modify
    
product = {'id': 1, 'name': 'laptop', 'price': 999.99}

structure = modify_dict(old_dict=product, in_stock=True)

print(structure)
print(type(structure))