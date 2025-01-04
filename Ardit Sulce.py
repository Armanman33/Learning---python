user_prompt = 'enter your todo'

todos = []

while True:
    todo = input(user_prompt)
    todos.append(todo)
    print(todo.title())
.
    password = input('Enter password')
while password != 'pass123':
    password = input('Enter password')
print('That is correct')
.
tedad = 0
while tedad <=6 :
    name = input('whats the name')
    tedad = tedad + 1
    print(name.capitalize())
print('gg', tedad)
.
countries = []

while True:
    country = input("Enter the country: ")
    countries.append(country)
    print(countries)
    .
    user_prompt = 'enter a todo, sir:'

todos = []

while True:
    todo = input(user_prompt)
    todos.append(todo)
    print(todos)
    .
    user_prompt = 'enter the name, sir:'

todos = []
tedad = 0

while True:
    tedad = tedad + 1
    country = input(user_prompt)
    todos.append(country)
    print(todos)
    if tedad > 6:
        break
    .

    todos = []

while True:
    user_selection = input('todo Robot says: Type add/show/exit/edit for your today todo list please.')

    match user_selection:
        case 'add':
            todo = input('What is your todo today?')
            todos.append(todo)
            #we append todos here because every definition is specific for its own case.it means we cant use todos.append in case show because we have not explained any todo function there.
        case 'show':
            print(todos)
            #why we can use todos here? it is because we`ve defined todos out of the match function so is usable for all parts of the code.
        case 'exit':
            break
        case 'edit':
            number = int(input('number of the todo from todo list that you want to edit:'))
            replace = input('what you want to put instead?')
            number = number - 1
            todos[number] = replace
            print('your replacation process has been done sucessfully')
print('bye,sir')
.
total_money =  float(input('How many dollars do you have?'))
euro = total_money * 2
print('Thanks for input. your total amount euro is', euro ,'with the exchange rate 2 !')
print(euro)
.
ranking = ['John', 'Sen', 'Lisa']
call = int(input('which rank you want to call?')) - 1
name = ranking[call]
print(name)
.
ranking = ['John', 'Sen', 'Lisa']
name = input('input the name:')
rank = ranking.index(name) + 1
print(rank)
.
names = ['John Smith', 'Jay Santi', 'Eva Kuki']
names = name.title() for name in names
    print(names)
.
usernames = ["john 1990", "alberta1970", "magnola2000"]
numbs = [len(item) for item in usernames]
    print(numbs)
.
user_entries = ['10', '19', '20']
#be in elat beyn adad '' gozashte mishe ke harkodum yek item hesab beshan
user_number = [float(item) for item in user_entries]
print(user_number)
.
user_entries = ['10', '19.1', '20']
sum_of_numbers = sum(float(entry) for entry in user_entries)
print(sum_of_numbers)
.
member = input('new member:')

file = open('members.txt','r')
existing_members = file.readlines()
file.close()

existing_members.append(member)

file = open('members.txt', 'w')
existing_members = file.writelines(existing_members)
file.close()
.
list = ['document' , 'file' , 'format']
for i,j in enumerate(list):
    print(f"{i+1}-{j.capitalize()}.txt")
.

while True:
    user_action = input('Type 1 or 2 for what you want.')

    match user_action:

        case '1':
            print('You chose 192.168.1.1')

        case '0':
            print('You chose 192.168.0.0')

            #or

ips = ['100.122.133.105', '100.122.133.111']

user_choice = int(input("Enter the index of the IP you want: "))
message = f"You chose {ips[user_choice]}"
print(message)

.

for i, j in enumerate("abcd"):
    print(j)
    #enumerate means yeka yek shomordan. baraye hamin in a b c d mikone o bekhater inke dakhele ye '' hastan yedune nemishmore.

.

contents = ['All carrots are to be sliced logitudinally.', 'The carrots were reportedly sliced.', 'The slicing process was well presented.']

filenames = ['doc.txt', 'report.txt', 'presentation.txt']

for content, filename in zip(contents,filenames):
    file = open(f".../files/{filename}", 'w')
    file.write(content)

.

file = open('essay.txt', 'r')
content = file.read()
print(content.title())

.

user_entries = ['10', '19.1', '20']
user_numbers = [float(item) for item in user_entries]
print(user_numbers)

.

user_entries = ['10', '19.1', '20']
sum_of_numbers = sum(float(entry) for entry in user_entries)
print(sum_of_numbers)

.

new = [i for i in ['a', 'b', 'c']]
print(new)

.

squared_numbers = [x**2 for x in range(10)]
#list comprehension exp
.

queue = ' a '
queue = queue.strip()
print(queue)
#this removes both side whitespaces

queue = ' a '
queue = queue.lstrip()
print(queue)
#this removes left side whitespaces

queue = ' a '
queue = queue.rstrip()
print(queue)
#this removes right side whitespaces
#this removing method doesnt work for items in []

.

with open("file.txt", 'w') as file:
    file.write("Hello")

with open("file.txt", 'w') as file:
    file.write("Hi")
    --> Hi

    #&&&&

    with open("file.txt", 'w') as file:
        file.write("Hello")
    file.write("Hi")
    --> HelloHi

.

#list slicing: starts from zero;
user_pulse = 'add clean the bag'
user_pulse[4:]
-> clean the bag
user_pulse[4:8]
-> clea
user_pulse[4:11]
clean t

.

date = input('Enter today`s date: ')
mood = input('How do you rate your mood today from 1 to 10? ')
thoughts = input('Let your thoughts flow:\n')

with open(f"../journal/{date}.txt", 'w') as file:
    file.write(mood + 2 * '\n')
    file.write(thoughts)

.

password = input('Enter new password: ')
result = []

if len(password) >= 8:
    result.append(True)
else:
    result.append(False)

digit = False
for i in password: #in yani tuye kole password migarde ye adad peyda kone
    if i.isdigit():
        digit = True

result.append(digit)

uppercase = False
for i in password: #in yani tuye kole password migarde ye harf bozorg peyda kone
    if i.isupper():
        uppercase = True

result.append(uppercase)

if all(result) == True:
    print(' /Strong Password\ ')
elif digit == False or uppercase == False or password == False:
    print(' *Moderate Password* ')
else:
    print('>Weak Password<')

.

password = input('Enter new password: ')
result = {}

if len(password) >= 8:
    result["length"] = True
else:
    result["length"] = False

digit = False
for i in password: #in yani tuye kole password migarde ye adad peyda kone
    if i.isdigit():
        digit = True

result["digits"] = digit

uppercase = False
for i in password: #in yani tuye kole password migarde ye harf bozorg peyda kone
    if i.isupper():
        uppercase = True

result["upper-case"] = uppercase

print(result)
print(result.values())

if all(result.values()):
    print(' <Strong Password> ')
else:
    print('>Weak Password<')

.

# Get user input for length and width
length = float(input("Enter length: "))
width = float(input("Enter width: "))

# Calculate perimeter and area
perimeter = (length + width) * 2
area = length * width

# Output the results
print("Perimeter is:", perimeter)
print("Area is:", area)

# Check conditions and print results
perimeter_condition = perimeter < 14
area_condition = area > 8

if perimeter_condition and area_condition:
    print("OK")
else:
    if not perimeter_condition:
        print("Perimeter is not OK. It is greater than or equal to 14.")
    if not area_condition:
        print("Area is not OK. It is less than or equal to 8.")

.

# Get user input for length and width
length = float(input("Enter length: "))
width = float(input("Enter width: "))

# Calculate perimeter and area
perimeter = (length + width) * 2
area = length * width

# Determine conditions
perimeter_condition = perimeter < 14
area_condition = area > 8

# Output the results with OK/NOT OK status
print("Perimeter is:", perimeter, "(OK)" if perimeter_condition else "(NOT OK)")
print("Area is:", area, "(OK)" if area_condition else "(NOT OK)")

# Final result
if perimeter_condition and area_condition:
    print("Final Result: Both conditions are OK.")
else:
    print("Final Result: NOT OK. One or both conditions are not satisfied.")

.

try:
    width = float(input('Enter rectangle width: '))
    length = float(input('Enter rectangle length: '))
    if width == length:
        exit('That looks like a square.')
    area = width * length
    print(area)
except ValueError:
    print('Please enter a number!')

.
try:
    value = float(input('Please enter your value:'))
    total_value = float(input('please enter your total value here:'))
    percentage = value / total_value * 100
    print(f"That is {percentage}")
except ValueError:
    print('Please use numbers.')

.

def get_max():
    grades = [9.6, 9.2, 9.7]
    maximum = max(grades)
    return maximum

print(get_max())

.

def get_max():
    grades = [9.6, 9.2, 9.7]
    maximum = max(grades)
    minimum = min(grades)
    message = f"Max: {maximum} and Min: {minimum}"
    return message

print(get_max())

.

feet_inches = input('Enter feet and inches: ')

def parse(feet_inches):
    parts = feet_inches.split(' ')
    feet = float(parts[0])
    inches = float(parts[1])
    return {"feet": feet, "inches": inches}


def convert(feet, inches):
    meters = feet * 0.3048 + inches * 0.0254
    return meters

parsed = parse(feet_inches)

result = convert(parsed['feet'], parsed['inches'])
print(f"{parsed['feet']} feet and {parsed['inches']} is equal to {result}")

if result < 1:
    print('Kids is too small.')
else:
    print('Kid can use the slide.')

.

def foo(mylist): #in yani to ye functenio moshakhas mikoni va ye arg barash mizari. va to qesmat return barash moshakhas mikoni
    # ke baraye arg che etefaqi biofte o harvaqt esm function ro seda zadi o to parantez chiz gozashti un etefaqa biofte.
    return sum(mylist) / len(mylist)
print(foo([10,20,30,40]))

.

def foo(name):
    return f"Hi {name}"
print(foo('Lisa'))

.

def get_name(name):
    return f"Greeting {name.capitalize()}"
print(get_name('Loyi'))

.

def get_age(year_of_birth, current_year=2024):
    return current_year - year_of_birth
print(get_age(2022, current_year ))
#Chera in code run nemishe? noktash ineke bad az return def tamum mishe va vaqti print ro call
#nemitune addad 2024 ro peyda kone. 2 ta rah hast ya qable print current_year = 2024 bezari ke mishe local
#ya in ke besurate global store koni. yani   age = current_year - year_of_birth . then return age


.

def get_age(year_of_birth, current_year=2024):
    age = current_year - year_of_birth
    return age
print(get_age(2022, current_year ))

.

def get_nr_items(user_input):
    items = user_input.split(',')
    return len(items)
print(get_nr_items('john,lisa'))

.

def masahat(k):
    return k * k
print(masahat(6))

.

def cw(temperature):
    if temperature > 7:
        return f"temp is {'warm'}"
    if temperature <= 7:
        return 'cold'
print(cw(55))

.

dictionary = {
    'Alex': 5,
    'Meysam': 7,
    'Lisa': 12,
    'Lexi': 24,
}
dictionary['John'] = 15

print('Alex`s age:', dictionary['Alex'])
print('All names in dictionary:', list(dictionary.keys()))
print('Full dictionary:', dictionary)
#print(dictionary['Alex'])
#print(dictionary.keys())
#print(dictionary.values())

.


warm = input('what is the temprature')
dictionary = {
    'warm': warm
}
print({'warm': warm})

.

def ww(password): #dakhele parantez yani parametr. bayad jay gozari beshe. argument jay gozari nemishe.
    if len(password) >= 8:
        return True
    else:
        return False
print(ww('password'))

.

def calculate_time(h, g=9.80665): #Non default argument should be listed first.
    t = (2 * h / g) ** 0.5
    return t


time = calculate_time(100)
print(time)

.

date = input('Enter today`s date: ')
mood = input('How is your mood today. say it by numbers: ')
thoughts = input('Share with me your thoughts: \n')

with open(f"../Journals/{mood}.txt", 'w') as file:
    file.write(date)
    file.write(thoughts)

.

def ww(temperature):
    if temperature > 0 and temperature < 100:
        return 'Liquid'
    if temperature <= 0:
        return 'Solid'
    if temperature >= 100:
        return 'Gas'

print(ww(99))

.

def water_state(temperature):
    if temperature <= 0:
        return "Solid"
    elif 0 < temperature < 100:
        return "Liquid"
    else:
        return "Gas"

.

freezing_point = 0
boiling_point = 100

def ww(temperature):
    if temperature > freezing_point and temperature < boiling_point:
        return 'Liquid'
    if temperature <= freezing_point:
        return 'Solid'
    if temperature >= 100:
        return 'Gas'

print(ww(99))

.

