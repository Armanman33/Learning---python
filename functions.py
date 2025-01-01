FILEPATH = 'todos.txt'


def get_todos(filepath="todos.txt"):#filepath = 'todos.txt'
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local
#2 line space between def and other parts of code.

def write_todos(todos_arg, filepath=FILEPATH):#jaye in 2 da moheme.
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == '__main__':
    print('Hello')
print('Hello from functions!')