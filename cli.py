from functions import get_todo,write_todo
import time

now=time.strftime("%b %d,%Y %H:%M:%S")
print("It is",now)
while True:
    case_match = input("Type add or show or edit or complete or exit: ").strip()

    if case_match.startswith('add'):
        todo = case_match[4:] + '\n'
        todos = get_todo()
        todos.append(todo)
        write_todo(todos)

    elif case_match.startswith('show'):
        todos = get_todo()
        for index, item in enumerate(todos, 1):
            print(index, item, end="")

    elif case_match.startswith('edit'):
        try:
            number = int(case_match[5:]) - 1
            todos = get_todo()
            new_item = input("Enter the new item: ") + "\n"
            todos[number] = new_item
            write_todo(todos)
        except ValueError:
            print("Please enter a valid number after 'edit'")
        except IndexError:
            print("Item number out of range")

    elif case_match.startswith('complete'):
        try:
            number = int(case_match[8:]) - 1
            todos = get_todo()
            todos.pop(number)
            write_todo(todos)
        except ValueError:
            print("Please enter a valid number after 'complete'")
        except IndexError:
            print("try to give the number in the todo range only")

    elif case_match.startswith('exit'):
        break
    else:
        print("hey wrong selection")
