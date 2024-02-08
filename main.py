from math import sqrt
from tkinter import *
from tkinter import ttk
import tkinter as tk

def btn_click(item):
    global expression
    try:
        input_field['state'] = "normal"
        expression += item
        input_field.insert(END, item)

        if item == '=':
            result = str(eval(expression[:-1]))
            input_field.insert(END, result)
            expression = ''

        input_field['state'] = "readonly"
    except ZeroDivisionError:
        input_field.delete(0, END)
        input_field.insert(0, 'ошибка (деление на 0)')
    except SyntaxError:
        input_field.delete(0, END)
        input_field.insert(0, "Ощибка")


def bt_clear():
    global expression
    expression = ""
    input_field['state'] = 'normal'
    input_field.delete(0, END)

root = Tk()
root.title("калькулятор")
root.geometry("170x264")
root.config(bg='#f2f2f2')

frame_input = Frame(root)
frame_input.grid(row=0, column=0, columnspan=4, sticky="nsew")

input_field = Entry(frame_input, font='Arial 15 bold', width=15, state="readonly", bg='#f2f2f2', borderwidth=0)
input_field.pack(fill=BOTH)
input_field["readonlybackground"] = '#f2f2f2'
input_field["justify"] = "right"
buttons = (('7', '8', '9', '/'),
           ('4', '5', '6', '*'),
           ('1', '2', '3', '-'),
           ('0', '.', '=', '+')
           )

expression = ""

button = Button(root, bg='#fff', text='C', borderwidth=0.1,  command=lambda: bt_clear())
button.grid(row=1, column=3, sticky="nsew")

for row in range(4):
    for col in range(4):
        Button(root, width=4, height=3, bg='#fff', borderwidth=0.1, text=buttons[row][col],
               command=lambda row=row, col=col: btn_click(buttons[row][col])).grid(row=row + 2, column=col, sticky="nsew", padx=1, pady=1)
root.mainloop()


