def get_todo():
    with open('todos.txt', 'r') as file:
        return file.readlines()


def write_todo(todos):
    with open('todos.txt', 'w') as file:
        file.writelines(todos)

if __name__=="__main__":
    print("hello")
    print(get_todo())