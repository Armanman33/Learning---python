def income(hour,per_hours):
    if per_hours > 10:
        return 'no way, get out!'
    elif per_hours <= 2:
        return 'why do you work for this?'
    elif hour > 15 and per_hours > 10:
        print('Good employee but high price sorry')
    elif hour > 15 and per_hours < 10:
        print('Good employee come in!')
    else:
        total_income = hour * per_hours
        return total_income

print(income(11,5))

---

i = 5
while True:
    print(i)
    i = i - 1
    if i <= 2:
        break

---

l = 32
while True:
    print(l)
    l = l + 1
    if l > 1000000:
        print('ff')
        break
print('gg')

---

for i in range(1,31):
    print(i)
    if i == 30:
        break
        print('gg')

---

e = ['debon' , 'arman' , 'erfan']
for bt in e:
    print('yo' , bt)

---

friends = ['debon' ,'arman' , 'erfan']
count = 0
for bs in friends:
    count = count + 1
    print('salam', bs)
print('I said' , count , 'heellooss')

---

x = input("number:")
x=int(x)
c=0
for i in range(1,x):
    if (x%i==0):
        c+=1
if (c==1):
    print("okey")

else:
    print("NOT okey")

---

tedad = 0
jam = 0
x = input('write number:')
while x != 'gg':
    tedad = tedad + 1
    x = int(x)
    jam = jam + x
    x = input('write number:')
    if x == 'gg':
        print('its over')
        break
print('your status', tedad , jam)
print('your ops', tedad/jam)

---

import random
javab = random.randint(1,99)
hads = input('what is your hads?')
hads = int(hads)

while hads != javab:
    if hads > javab:
        print('yours is larger')
    else:
        print('mine is larger')
    hads = input('what is your hads?')
    hads = int(hads)
print('gg')

---

import random
a = random.randint(1,10)
if a % 2 != 0:
    print('aval' , a)
else:
    print('morakab' , a)

---

blockchain = [2,8,3]
blockchain[1] --> 2
exmp = blockchain[2] + 0.3 = 3.3


...
blockchain = []


def get_last_blockchain_value():
    return blockchain[-1]


def addvalue(transaction_amount, last_transaction=[1]):
    blockchain.append([last_transaction, transaction_amount])

def get_transaction_value():
    return float(input('Your transaction amount?:'))


def get_user_choice():
    user_input = input('your choice:')
    return user_input


def print_blockchain_elements():
    for block in blockchain:
        print('outputting block')
        print(block)


tx_amount = get_user_choice()
addvalue(tx_amount)

while True:
    print('please choose:')
    print('1: add a new transaction value')
    print('2:out put the blockchain blocks')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_amount = get_transaction_value()
        addvalue(tx_amount, get_last_blockchain_value())
    else:
        print_blockchain_elements()


    print('Done')

    user_prompt = 'enter your code'

todos = []

while True:
    todo = input(user_prompt)
    todos.append(todo)
    print(todo.title())

.

todos = []

while True:
    user_action = input('Type add/show/edit/exit/complete for your process:')
    user_action = user_action.strip()

    match user_action:
#case does not accept expressions through case. case only accept strings.
        case 'add':
            todo = input('what is your todo today?') + '\n'

            #file = open('todos.txt', 'r')
            #todos = file.readlines()
            #file.close()

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            #file = open('todos.txt', 'w')
            # this creates file with that name.
            #file.writelines(todos)
            # this writes (todos) things in file.
            #with this function called between ()
            #file.close()

            with open('todos.txt', 'w') as file:
                file.writelines(todos)


        case 'show':
            #file = open('todos.txt', 'r')
            #todos = file.readlines()
            #file.close()

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            #new_todos = [item.strip('\n') for item in todos]

            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index + 1}-{item}"
                print(row)

        case 'edit':
            number = int(input(' which number u want to edit?:'))
            number = number - 1

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            replace = input('what u want to put instead?:')
            todos[number] = replace

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case 'complete':
            number = int(input(' which number u want to complete?:'))

            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            index = number - 1
            todo_to_remove = todos[index].strip('\n') #\n creates a great empty line.
            todos.pop(index)

            todos.pop(number - 1) #.pop removes the last item from index, as default the last one.

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

            message = f"todo {todo_to_remove} was removed from the list."
            print(message)

        case 'exit':
            break






print('Bye sir!')

.

def get_area(x=10):
    return x * 2

area = get_area()
print(area)

.



