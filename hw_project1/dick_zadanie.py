# задание
# Есть список словарей со студентами `students`. В каждом объекте есть имя и фамилия студента,
# а также список оценок (целых чисел). Нужно написать функцию get_best_students, которая берёт студентов и находит того,
# у кого средний балл наибольший. Возвращает функция список студентов с лучшим баллом. У некоторых студентов в оценках
# есть None: их среднюю оценку мы считаем равной 0.


students = [
    {
        "name": "John", 
        "surname": "Doe", 
        "grades": [5, 5, 4, 4]
    },
    {"name": "Jane", "surname": "Doe", "grades": [4, 3, 4, 3, 5]},
    {"name": "Bill", "surname": "Gates", "grades": [5, 5, 5, 3]},
    {"name": "Steve", "surname": "Jobs", "grades": [3, 5, 4, 8, 3, 5]},
    {"name": "Guido", "surname": "Van Rossum", "grades": [5, 3, 5, 4, 5, 5, 3, 5]},
    {"name": "Elon", "surname": "Musk", "grades": None}
]



# решение
super_counter = 0
for i in students:
    grades = i.get("grades")

    if grades is None:
        grades = [0]

    counter = 0
    for j in grades:
        counter += j

    result = counter / len(grades)
    
    if result > super_counter:
        super_counter = result
    i["avg"] = result



print(super_counter)

for i in students:
    if i.get("avg") == super_counter:
        print(f"{i.get("name")} {i.get("surname")}")

