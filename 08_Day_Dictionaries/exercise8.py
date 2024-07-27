person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
print(len(person))

print(person['first_name']) # Asabeneh
print(person['country'])    # Finland
print(person['skills'])     # ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person['skills'][0])  # JavaScript
print(person['address']['street']) # Space street
print(person['address'])
print(person['address']['zipcode'])
print(person.get('first_name')) # Asabeneh
print(person.get('country'))    # Finland
print(person.get('skills')) #['HTML','CSS','JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person.get('city'))   # None
person['job_title'] = 'Instructor'
person['skills'].append('HTML')
print(person)
person['first_name'] = 'Eyob'
person['age'] = 252
print('age' in person)
print('gender' in person)
person.pop('first_name')        # Removes the firstname item
person.popitem()                # Removes the address item
del person['is_marred']        # Removes the is_married item

print(person.items())
print(person.clear())
del person

dog={}
print(type(dog))
dog={'name':'lucky',
     'color':'yellow',
     'breed':'country dog',
     'legs':4,
     'age':10}
import random

# Lists of possible Icelandic names and other details
icelandic_first_names = ["Ari", "Björn", "Einar", "Guðrún", "Helga", "Íris", "Jón", "Kristín", "Magnús", "Nanna"]
icelandic_last_names = ["Jónsson", "Sigurðardóttir", "Gunnarsson", "Björnsdóttir", "Ólafsson", "Karlsdóttir", "Þórðarson", "Guðmundsdóttir"]
icelandic_cities = ["Reykjavík", "Kópavogur", "Hafnarfjörður", "Akureyri", "Reykjanesbær", "Garðabær", "Mosfellsbær"]
skills = ["Programming", "Data Analysis", "Web Design", "Icelandic Literature", "Geology", "Fishing", "Skiing", "Volcanic Studies"]

# Create the student dictionary
student = {
    "first_name": random.choice(icelandic_first_names),
    "last_name": random.choice(icelandic_last_names),
    "gender": random.choice(["Male", "Female", "Non-binary"]),
    "age": random.randint(18, 30),
    "marital_status": random.choice(["Single", "In a relationship", "Married"]),
    "skills": random.sample(skills, k=random.randint(1, 4)),
    "country": "Iceland",
    "city": random.choice(icelandic_cities),
    "address": f"{random.randint(1, 100)} {random.choice(['Aðalstræti', 'Laugavegur', 'Skólavörðustígur', 'Bankastræti'])} St."
}

print(student)
print(len(student))
student_skills=student["skills"]
print(type(student_skills))
student['skills'].append('Mountain-climbing')
print(student.keys())
print(student.values())
print(type(student.keys()))
print(student.items())
del student['gender']
del student