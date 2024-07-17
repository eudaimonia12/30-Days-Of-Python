print(len("Hello, World!"))
print(type(str(10)))
print(type(int("10")))
# Variables in Python

first_name = 'Asabeneh'
last_name = 'Yetayeh'
country = 'Finland'
city = 'Helsinki'
age = 250
is_married = True
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
    'firstname':'Asabeneh', 
    'lastname':'Yetayeh', 
    'country':'Finland',
    'city':'Helsinki'
    }

# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)
print("It's a beautiful day")  # Using double quotes to contain a string with a single quote
print('He said, "Hello!"')     # Using single quotes to contain a string with double quotes
print("He said, 'Hello!'")

# Declaring multiple variables in one line

first_name, last_name, country, age, is_married = 'Asabeneh', 'Yetayeh', 'Helsink', 250, True

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)

name = "Alice"
print(f'Hello, {name}!')  # Using single quotes for the f-string
message = 'Hello' " " 'World'  # This is valid and results in "Hello World"
print(message)

# casting
# int to float
num_int = 10
print('num_int',num_int)         # 10
num_float = float(num_int)
print('num_float:', num_float)   # 10.0

# float to int
gravity = 9.81
print(int(gravity))             # 9

# int to str
num_int = 10
print(num_int)                  # 10
num_str = str(num_int)
print(num_str)                  # '10'

# str to int or float
num_str = '10.6'
print('num_float', float(num_str))  # 10.6

# str to list
first_name = 'Asabeneh'
print(first_name)               # 'Asabeneh'
first_name_to_list = list(first_name)
print(first_name_to_list)            # ['A', 's', 'a', 'b', 'e', 'n', 'e', 'h']

#exercise
num_one=5
num_two=4
total=num_one+num_two
diff=num_one-num_two
product=num_one*num_two
division=num_one/num_two
remainder=num_one%num_two
exp=num_one**num_two
floor_division=num_one//num_two
print(total,diff,product,division,remainder,exp,floor_division)

import math
print(math.pi)
radius=30
area_of_circle=(math.pi)*(30**2)
circum_of_circle=(math.pi)*(30*2)
print(area_of_circle,circum_of_circle)