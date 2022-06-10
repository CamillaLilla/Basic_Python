friends = int(input('how many friends at your house?'))
pizzas = friends * 0.5
print('you need {} pizzas for {} friends.'.format(pizzas, friends))

mars_choice = input('Would you like to visit Mars? y/n ')
is_willing = mars_choice == 'y'
affordable = input('Can you afford to visit Mars? y/n ')
can_afford = affordable == 'y'
should_visit_mars = is_willing and can_afford
print('You should visit Mars: {}'.format(should_visit_mars))

price = input('How much is a burger? ')
vegetarian = input('Is there a vegetarian option? (y/n) ')
within_budget = float(price) <= 10.00
has_vegetarian = vegetarian == 'y'
is_good_choice = within_budget and has_vegetarian
if is_good_choice:
    print('This restaurant is a great choice!')
if not is_good_choice:
    print('Probably not a good idea')

name = input("What is your name? ")
is_admin = name == 'admin'
password = input("What is your password? ")
is_password_correct = password == '4dm1n'
if is_admin and is_password_correct:
    print('Welcome')
if not is_admin or not is_password_correct:
    print('Go away')

#alternatively

name = input("What is your name? ")
is_admin = name == 'admin'
password = input("What is your password? ")
is_password_correct = password == '4dm1n'
if is_admin and is_password_correct:
    print('Welcome')
else:
    print('Go away')

meal_price = float(input('How much did the meal cost? '))
discount_choice = input('Do you have a discount? y/n ')
is_discount = discount_choice == 'y'
is_over_twenty = meal_price >= 20.0
discount_applicable = is_discount and is_over_twenty
if discount_applicable:
    meal_price = meal_price * 0.9
    print('Discount applied')
else:
    print('No discount')
    print('Total cost: {}'.format(meal_price))

dog_size = int(input('How big is the dog? '))
if dog_size > 75:
    print('That is a big dog')
elif dog_size < 10:
    print('That dog could fit in my pocket')
elif dog_size < 25:
    print('That is a small dog')
else:
    print('That is an average dog')

