# how to change objects in a list:

clothes = ["shorts", "shoes", "t-shirt",
           ]
if clothes[0] == 'shorts':
    clothes[0] = 'warm coat'
print(clothes)

# list functions:
costs = [1.2, 4.3, 2.0, 0.5]
print(len(costs))
print(max(costs))
print(min(costs))
print(sorted(costs))
print(list(reversed(costs)))

# Search for items in a list:
student_name = input('Which student are you looking for? ')
students = [
    'Diedre', 'Hank', 'Helena', 'Salome',
]
if student_name in students:
    print('{} is in the class'.format(student_name))
else:
    print('{} is not in the class'.format(student_name))

fridge = [
    'cheese',
    'pizza',
    'coke',
]
if 'milk' not in fridge:
    print('You have no milk in the fridge')

# Add items to a list:

students = [
    'Diedre', 'Hank', 'Helena', 'Salome',
]
student_name = input('What is the name of the new student? ')
students.append(student_name)
print(students)

shopping_list = [
    'bread',
    'cheese',
    'pop tarts',
    'carrots',
]
if 'bread' in shopping_list:
    shopping_list.append('butter')
print('Your shopping list: ', shopping_list)

#For Loops:
student_names = ['Diedre', 'Hank', 'Helena', 'Salome']
for student_name in student_names:
    print(student_name)

student_names = ['Diedre', 'Hank', 'Helena', 'Salome']
count = 0
for student_name in student_names:
    count = count + 1
print(count)

costs = [8.30, 7.12, 5.01, 1.00, 0.99, 5.92, 3.50]
total_cost = 0
for cost in costs:
    total_cost = total_cost + cost
print(total_cost)
