from tkinter import Listbox

from functions import get_todo,write_todo
import os
os.environ['TCL_LIBRARY'] \
    = r'C:\Users\Kaushik\AppData\Local\Programs\Python\Python313\tcl\tcl8.6'
import FreeSimpleGUI

label=FreeSimpleGUI.Text("Type in a to-do")
input_box=FreeSimpleGUI.InputText(tooltip="Enter todo",key="todo")
add_button=FreeSimpleGUI.Button("Add")
list_box=FreeSimpleGUI.Listbox(values=get_todo(),key="todos",
                               enable_events=True,size=[45,10])
edit_button=FreeSimpleGUI.Button("Edit")
complete_button=FreeSimpleGUI.Button("Complete")
exit_button=FreeSimpleGUI.Button("Exit")
#add_show=FreeSimpleGUI.Button("show")


window=FreeSimpleGUI.Window('My To-Do App',
                            layout=[[label],
                                    [input_box,add_button],
                                    [list_box,edit_button,complete_button],
                                    [exit_button]]
                            ,font=('Helvetica',20))

while True:
    event,values=window.read()
    match event:
        case "Add":
            todos=get_todo()
            new_todo=values['todo'] + "\n"
            todos.append(new_todo)
            write_todo(todos)
            window['todos'].update(values=todos)
        case "Edit":
            todo_to_edit=values['todos'][0]
            new_todo=values['todo']
            todos=get_todo()
            index=todos.index(todo_to_edit)
            todos[index]=new_todo
            write_todo(todos)
            window['todos'].update(values=todos)
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case "Complete":
            todo_to_edit = values['todos'][0]
            todos=get_todo()
            todos.remove(todo_to_edit)
            write_todo(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value="")
        case "Exit":
            exit()
        case FreeSimpleGUI.WIN_CLOSED:
            break
window.close()