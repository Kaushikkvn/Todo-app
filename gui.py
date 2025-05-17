from functions import get_todo,write_todo
import os
os.environ['TCL_LIBRARY'] \
    = r'C:\Users\Kaushik\AppData\Local\Programs\Python\Python313\tcl\tcl8.6'



import FreeSimpleGUI

label=FreeSimpleGUI.Text("Type in a toa-do")
input_box=FreeSimpleGUI.InputText(tooltip="Enter todo",key="todo")
add_button=FreeSimpleGUI.Button("Add")
#add_show=FreeSimpleGUI.Button("show")


window=FreeSimpleGUI.Window('My To-Do App',
                            layout=[[label],[input_box,add_button]]
                            ,font=('Helvetica',20))

while True:
    event,values=window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos=get_todo()
            new_todo=values['todo'] + "\n"
            todos.append(new_todo)
            write_todo(todos)
        case FreeSimpleGUI.WIN_CLOSED:
            break
window.close()