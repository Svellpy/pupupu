# reshenie s nulya

flat_number = 80

entrance_number = flat_number // 20 
floor_number = flat_number % 20 // 4
print(entrance_number)
print(floor_number)

#
fruits = ["apple", "cherry", "banana", "watermelon"]
print(fruits[3])
print(fruits[-4])

#
fruits = ["apple", "cherry", "banana", "watermelon"]
fruits[0] = "pineapple"
print(fruits)

#
fruits = ["apple", "cherry", "banana", "watermelon"]
fruits[0], fruits[3] = fruits[3], fruits[0]

print(fruits)

#
numbers = [0, 1, 2, 3, 4, 5, 6, 7 ,8 ,9]
new_numbers = numbers[0:5]

print(new_numbers)
#print(numbers[0:5])

# 
numbers = [0, 1, 2, 3, 4, 5, 6, 7 ,8 ,9]
new_numbers = numbers[0:len(numbers)]
new_numbers2 = numbers[::2]

print(new_numbers2)
print(new_numbers)

#
numbers = [0, 1, 2, 3, 4, 5, 6, 7 ,8 ,9]
print(numbers[0:20])
print(numbers[::-1])

# 
string = "Hello, word"
print(string[5:])
print(string[::2])

#
numbers = [0, 1, 2, 3, 4, 5, 6, 7 ,8 ,9]

new_numbers = list(reversed(numbers))
print(type(new_numbers))
print(new_numbers)
