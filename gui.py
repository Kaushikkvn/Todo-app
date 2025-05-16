import modules.functions
import os
os.environ['TCL_LIBRARY'] = r'C:\Users\Kaushik\AppData\Local\Programs\Python\Python313\tcl\tcl8.6'

import tkinter as tk
tk.Tk().mainloop()
import FreeSimpleGUI

label=FreeSimpleGUI.Text("Type in a to-do")
input_box=FreeSimpleGUI.InputText(tooltip="Enter todo")
add_button=FreeSimpleGUI.Button("Add")
window=FreeSimpleGUI.Window('My To-Do App',layout=[[label,input_box,add_button]])
window.read()
window.close()