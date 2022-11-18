#Stores a colleciton of labelled items. Each item has a key and a value

person = {
'name': 'Jessica',
'age': 23,
'height': 172
}

print(person['name'])

place = {
'name': 'The Anchor',
'post_code': 'E14 6HY',
'street_number': '54',
'location': {
'longitude': 127,
'latitude': 63,
}
}
print(place['name'])
print(place['post_code'])
print(place['street_number'])

print(place['location']['longitude'])
print(place['location']['latitude'])

location = place['location']
print(location['longitude'])
print(location['latitude'])

#Putting dictionaries in lists
people = [
{'name': 'Jessica', 'age': 23},
{'name': 'Trisha', 'age': 24},
]
for person in people:
    print(person['name'])
    print(person['age'])

fruits = [
{'name': 'apple', 'colour': 'red', 'price': 0.12},
{'name': 'banana', 'colour': 'yellow', 'price': 0.2},
{'name': 'pear', 'colour': 'green', 'price': 0.19},
]
for fruit in fruits:
    print(fruit['name'])
    print(fruit['colour'])
    print(fruit['price'])


#Random Choice
import random
colours = ['red', 'green', 'blue']
chosen_colour = random.choice(colours)
print(chosen_colour)

