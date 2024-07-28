a = 3
if a > 0:
    print('A is a positive number')

# A is a positive number
a = 3
if a < 0:
    print('A is a negative number')
else:
    print('A is a positive number')

a = 0
if a > 0:
    print('A is a positive number')
elif a < 0:
    print('A is a negative number')
else:
    print('A is zero')

a = 3
print('A is positive') if a > 0 else print('A is negative') # first condition met, 'A is positive' will be printed

a = 0
if a > 0:
    if a % 2 == 0:
        print('A is a positive and even integer')
    else:
        print('A is a positive number')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative number')

#We can avoid writing nested condition by using logical operator and.
a = 0
if a > 0 and a % 2 == 0:
        print('A is an even and positive integer')
elif a > 0 and a % 2 !=  0:
     print('A is a positive integer')
elif a == 0:
    print('A is zero')
else:
    print('A is negative')

user = 'James'
access_level = 3
if user == 'admin' or access_level >= 4:
        print('Access granted!')
else:
    print('Access denied!')

#Exercise
user_age=int(input('Enter your age: '))
if user_age>=18:
     print('You are old enough to learn to drive.')
elif 18-user_age>1:
     print(f'You need {18-user_age} more years to learn to drive.')
else:
     print('You need one more year to learn to drive.')

your_age=int(input('Enter your age: '))
my_age=25
if my_age-your_age>1:
     print(f'You are {my_age-your_age} years younger than me.')
elif my_age-your_age==1:
     print('You are one year younger than me.')
elif my_age==your_age:
     print('We are the same age.')
elif my_age-your_age<1:
     print(f'You are {abs(my_age-your_age)} years older than me.')
elif my_age-your_age==-1:
     print('You are one year older than me.')   

first_number=int(input('Enter number one: '))
second_number=int(input('Enter number two: '))
if first_number>second_number:
     print(f'{first_number} is greater than {second_number}.')
elif first_number<second_number:
     print(f'{second_number} is greater than {first_number}.')
else:
     print('They re equal!')

#level 2
score=int(input("Please enter your score(0~100): "))
if 90<=score<=100:
     print('A')
elif 70<=score<=89:
     print('B')
elif 60<=score<=69:
     print('C')
elif 50<=score<=59:
     print('D')
else:
     print('F')

fruits = ['banana', 'orange', 'mango', 'lemon']
new_fruit=input("Enter the name of a fruit: ")
if new_fruit in fruits:
     print('That fruit already exist in the list')
else:
     fruits.append(new_fruit)
     print(fruits)

#Level 3
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
if person['skills']:
     print(person['skills'])
     skill_lst=person['skills']
     if 'Python' in skill_lst:
          print('true')
     else:
          print('cannot do Python')
     if   'Javascript' in skill_lst and 'React' in skill_lst and len(skill_lst)==2:
          print('He is a front end developer') 
     if 'Node' in skill_lst and 'Python' in skill_lst and 'MongoDB' in skill_lst and not 'React' in skill_lst:
          print('He is a backend developer')
     if 'React' in skill_lst and 'Node' in skill_lst and 'MongoDB' in skill_lst:
          print('He is a fullstack developer')
     else:
          print('unknown title')
if person['country']=='Finland' and person['is_marred']==True:
     print(f'{person["first_name"]} {person["last_name"]} lives in Finland. He is married.')