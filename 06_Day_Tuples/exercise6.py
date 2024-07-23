fruits = ('banana', 'orange', 'mango', 'lemon')
# syntax
tpl = ('item1', 'item2', 'item3')
print(len(tpl))
fruits = ('banana', 'orange', 'mango', 'lemon')
first_fruit = fruits[0]
second_fruit = fruits[1]
last_index =len(fruits) - 1
last_fruit = fruits[last_index]
fruits = ('banana', 'orange', 'mango', 'lemon')
first_fruit = fruits[-4]
second_fruit = fruits[-3]
last_fruit = fruits[-1]
fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[0:4]    # all items
all_fruits= fruits[0:]      # all items
orange_mango = fruits[1:3]  # doesn't include item at index 3
orange_to_the_rest = fruits[1:]
fruits = ('banana', 'orange', 'mango', 'lemon')
print('orange' in fruits) # True
print('apple' in fruits) # False
#fruits[0] = 'apple' # TypeError: 'tuple' object does not support item assignment
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
fruits_and_vegetables = fruits + vegetables
fruits = ('banana', 'orange', 'mango', 'lemon')
del fruits

#exercise
empty_tuple=()
print(type(empty_tuple))
sister=('emma','everlyn')
brother=('jackie','joseph')
sibling=sister+brother
print(sibling)
print(len(sibling)
      )
family=list(sibling)
family.append('eva')
family.append('lucas')
print(family)

family=('emma', 'everlyn', 'jackie', 'joseph', 'eva', 'lucas')
sibling=family[0:4]
parents=family[-2:]
print(sibling,parents)

fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
animal_products=('beef','pork','chicken')
food_stuff_tp = fruits + vegetables+animal_products
food_stuff_lst=list(food_stuff_tp)
print(len(food_stuff_tp))
print(food_stuff_tp[5],food_stuff_lst[6])
print(food_stuff_tp[0:3],food_stuff_tp[-3:])
del food_stuff_tp
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)