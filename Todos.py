#from functions import get_todos, write_todos
import functions # age to ye directory dg bud az from ham estfde mikonim.
import time

now = time.strftime('%b %d, %Y %H:%M:%S')
while True:
    user_action = input('Type add, show, edit, complete or exit for your process:')
    user_action = user_action.strip()


    if user_action.startswith("add"):
        todo = user_action[4:] #this means bring the thing with 4 number.

        #file = open('todos.txt', 'r')
        #todos = file.readlines()
        #file.close()

        todos = functions.get_todos()

        todos.append(todo + '\n')
        
        #file = open('todos.txt', 'w')
        # this creates file with that name.
        #file.writelines(todos)
        # this writes (todos) things in file.
        #with this function called between ()
        #file.close()

        functions.write_todos(filepath='todos.txt', todos_arg=todos)


    elif user_action.startswith("show"):
        #file = open('todos.txt', 'r')
        #todos = file.readlines()
        #file.close()

        todos = functions.get_todos()

        #new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith("edit"):
        try: #this means run these lines below. but if...
            number = int(user_action[5:]) #e:0 d:1 i:2 t:3 :4 userinput:5
            print(number)

            number = number - 1

            todos = functions.get_todos()

            replace = input('what u want to put instead?:')
            todos[number] = replace + '\n'

            functions.write_todos('todos.txt', todos)
        except ValueError: #if there is an error ( we specified error ) then run this 2 line below.
            print('Your command is not valid')
            continue #And this means loop the circle ( opposite function of: break ) until user runs 'edit' well.

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            
            todos = functions.get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip('\n') #\n creates a great empty line.
            todos.pop(index) #.pop removes the last item from index, as default the last one.

            functions.write_todos(todos)

            message = f"todo {todo_to_remove} was removed from the list."
            print(message)
        except IndexError:
            print('There is no item with that number.')
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print('Command is not valid')

print('Bye sir!')