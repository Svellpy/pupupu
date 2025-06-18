operations = {
    "+": "сложение",
    "-": "вычитание",
    "*": "умножение",
    "/": "деление",
    "**": "возведение в степень",
    "@": "извлечение квадратного корня",
    "0": "выкл"
}

print("Доступны операции:")
for op, desc in operations.items():
    print(f"  {op} - {desc}")

while True:

    operation = str(input("Выберите тип операции:\n"))


    if operation not in operations:
        print("Заюш, ты что в глаза долбишься\nПеречитай список разрешенных операций\n")
        continue



    
    number_1 = float(input("Введите первое число:\n"))


    if operation != "@":
        number_2 = float(input("Введите второе число:\n"))




    if operation == "*":
        print(f"Решение: {number_1 * number_2}")
    elif operation == "/":
        if number_2 == 0:
            print("Заюш, на ноль делить нельзя\nПопробуй ещё раз\n")
            continue
        print(f"Решение: {number_1 / number_2}")
    elif operation == "+":
        print(f"Решение: {number_1 + number_2}")
    elif operation == "-":
        print(f"Решение: {number_1 - number_2}")
    elif operation == "**":
        print(f"Решение: {number_1 ** number_2}")
    elif operation == "@":
        print(f"Решение: {number_1 ** 0.5}")
    elif operation == "0":
        break