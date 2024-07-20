language = 'Python'
last_letter1 = language[-1]
last_letter2 = language[5]
print(last_letter1 ,last_letter2)
print(last_letter1==last_letter2)

greeting = 'Hello, World!'
print(greeting[0:])
print(greeting[-1:])
print(greeting[::-1]) # !dlroW ,olleH

name='bronco'
half=name[0:6:2]
other_half = name[1:6:2]
other_half_another_way=name[1::2]
print(half)
print(other_half)
print(other_half_another_way)
print(name.count('o'))
print(name.endswith('co'))
print(name.find('o'))
print(name.rfind('o'))

s0,s1,s2,s3= 'Thirty','Days', 'Of', 'Python'
print(s0+s1+s2+s3)
print(s0,s1,s2,s3)
ss0,ss1,ss2='Coding', 'For' , 'All'
print(ss0+' '+ss1+' '+ss2)
company="Coding For All"
print(company)
print(len(company))
print(company.upper(),company.lower())
print(company.capitalize(), company.title(),company.swapcase())
print(company[0:6])
print(company.find('Coding'))
print(company.index('Coding'))
print(company.replace('Coding','Python'))
print('Python for Everyone'.replace('Everyone','All'))
print(company.split())
print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(','))
print(company[0])
print(company[-1])
print(company[10])
print(company[0]+company[7]+company[11])
print(company.find('C'))
print(company.index('C'))
print(company.find('F'))
print(company.rfind('l'))
print( 'You cannot end a sentence with because because because is a conjunction'.find('because'))
print( 'You cannot end a sentence with because because because is a conjunction'.rfind('because'))
sentence = "You cannot end a sentence with because because because is a conjunction"

# Find the starting index of the first 'because'
start_index = sentence.find("because")
# Extract 23 characters from the starting index (7 characters per 'because' * 3 + space*2)
phrase = sentence[start_index:start_index + 23]
print(phrase)

print(company.startswith('Coding'))
print(company.startswith('coding'))
print('   Coding For All      '.strip(' '))
print('30DaysOfPython'.isidentifier())
print('thirty_days_of_python'.isidentifier())
libraries=['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
result=" ".join(libraries)
print(result)
print('I am enjoying this challenge.\nI just wonder what is next.')
print('Name\tAge\tCountry\tCity\nAsabeneh250\tFinland\tHelsinki')
radius = 10
area = 3.14 * radius ** 2
print('The area of a circle with radius {} is {} meters square.'.format(radius,area))
num1=8
num2=6
print(f'{num1}+{num2}={num1+num2}')
print(f'{num1}-{num2}={num1-num2}')
print(f'{num1}*{num2}={num1*num2}')
print(f'{num1}/{num2}={num1/num2:.2f}')
print(f'{num1}%{num2}={num1%num2}')
print(f'{num1}//{num2}={num1//num2}')
print(f'{num1}**{num2}={num1**num2}')