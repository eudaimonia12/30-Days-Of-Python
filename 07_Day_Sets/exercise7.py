# syntax
st = {'item1', 'item2', 'item3', 'item4'}
# syntax
fruits = {'banana', 'orange', 'mango', 'lemon'}
print(len(fruits))
print('banana' in fruits)
print('kiwifruit' in fruits)
fruits.add('kiwifruit')
print('kiwifruit' in fruits)
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
fruits.update(vegetables)
print(fruits)
fruits.remove('lemon')
fruits.pop()  # removes a random item from the set
removed_item = fruits.pop()
print(removed_item)
fruits.clear()
print(fruits) # set()
fruits = {'banana', 'orange', 'mango', 'lemon'}
del fruits
fruits = ['banana', 'orange', 'mango', 'lemon','orange', 'banana']
fruits = set(fruits) # {'mango', 'lemon', 'banana', 'orange'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
print(fruits.union(vegetables))

fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
fruits.update(vegetables)
print(fruits) # {'lemon', 'carrot', 'tomato', 'banana', 'mango', 'orange', 'cabbage', 'potato', 'onion'}

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.intersection(even_numbers) # {0, 2, 4, 6, 8, 10}

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
print(python.intersection(dragon) )   # {'o', 'n'}

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.difference(even_numbers) # {1, 3, 5, 7, 9}

python = {'p', 'y', 't', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.difference(dragon)     # {'p', 'y', 't'}  - the result is unordered (characteristic of sets)
dragon.difference(python)     # {'d', 'r', 'a', 'g'}

#exercise
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
print(len(it_companies))
it_companies.add('Twitter')
it_companies2={'OpenAI','Nvidia','uber'}
it_companies.update(it_companies2)
print(it_companies)
it_companies3={'dell','adobe','oracle','hp','sony'}
print(it_companies.union(it_companies3))
it_companies.remove('Oracle')
removed_item=it_companies.pop()
print(removed_item)
print(it_companies)

C=A.union(B)
print(A.intersection(B))
print(A.issubset(B))
print(A.isdisjoint(B))
print(A.union(B))
print(B.union(A))
print(A.symmetric_difference(B))
del A
del B

age_set=set(age)
print(len(age_set)-len(age)) #sets can only contain unique items
sentence='I am a teacher and I love to inspire and teach people'
word_lst=sentence.split()
word_set=set(word_lst)
print(len(word_set))