# #
# def my_function():
#     local_var = "I'm local variable"
#     print(local_var)



# my_function()

# #
# variable = "i'm variable uot of scope"


# def my_function():
#     variable = "i'm a local variable inside function"
#     print(variable)

# my_function()

# #
# COMFORTABLE_TEMPERATURE = 25


# def get_diff_from_comfortable_temperature(*, temperature: int) -> int:
#     return COMFORTABLE_TEMPERATURE - temperature

# print(get_diff_from_comfortable_temperature(temperature=20))

#
DEFAULT_LEVEL_EXPERIENCE = 200


def is_level_up(*, current_experience: int, gained_experience: int,) -> bool:
    total_experience = current_experience + gained_experience
    level_up = False

    if total_experience >=  DEFAULT_LEVEL_EXPERIENCE:
        level_up = True

    return level_up


print(is_level_up(current_experience=150, gained_experience=60))
print(is_level_up(current_experience=10, gained_experience=60))