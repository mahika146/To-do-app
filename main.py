from functions import get_todos, write_todos
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True:
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:].strip()

        todos = get_todos()

        todos.append(todo + '\n')
        write_todos(todos)

    elif user_action == 'show':
        todos = get_todos()
        for index, item in enumerate(todos):
            row = f'{index + 1}. {item.strip()}'
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number -= 1
            print(number)

            todos = get_todos()
            new_todo = input("Enter a new todo: ").strip()
            todos[number] = new_todo + '\n'
            write_todos(todos)
        except ValueError:
            print('Your command is not valid.')
            continue


    elif user_action.startswith('complete'):
        try:
            number = int(input("Number of the todo to complete: "))
            index = number - 1

            todos = get_todos()
            todo_to_remove = todos[index].strip()

            todos.pop(index)
            write_todos(todos)

            message = f"Todo '{todo_to_remove}' was removed"
            print(message)
        except IndexError:
            print("There is no item with that number")
            continue


    elif user_action == 'exit':
        break

print('Bye')
