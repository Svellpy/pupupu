#
file_names = ["document1.txt", "image1.jpg", "document2.txt", "image2.jpg"]

for file_name in file_names:    
    print(file_name)

#
greeting ="Hello,world!"
count_o = 0
for char in greeting:   
    if char == "o":
        count_o += 1
        print(char)
print(count_o)

#
greeting ="Hello,world!"
for char in greeting:
    print(char)

#
students = ["Alice", "Bob", "Charlie", "David"]

for student in students:
    print(student)
    for char in student:
        print(char)

#
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

for num in numbers:
    if num % 2 == 0:
        continue
    print(num)

#
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

for num in numbers:
    if num == 10:
        break
    print(num)

#
range_object = range(10)
print(range_object)

numbers = list(range_object)
print(numbers)

#
my_range = range(1, 10, )
print(list(my_range))

#
my_range = range(1, 10, 2)
print(list(my_range))

#
my_range = range(10, 1, -1)
print(list(my_range))

#
numbers = [10, 11, 12, 13, 14, 15]

for i in range(len(numbers)):
    numbers[i] += 1

print(numbers)

#
greeting = "Hello, world!"

indexes = []
count = 0

for i in range(len(greeting)):
    if greeting[i] == "o":
        count += 1
        indexes.append(i)

print(count)
print(indexes)
