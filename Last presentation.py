from tkinter import *

root = Tk()
root.title('Simple Calculator')
root.config(bg="Brown")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_click(number):
    e.insert(END, number)

def button_clear():
    e.delete(0, END)

def button_add():
    e.insert(END, '+')

def button_equal():
    try:
        expression = e.get()
        if '*' in expression and '%' in expression:
            parts = expression.split('*')
            number = float(parts[0].strip())
            percentage = float(parts[1].split('%')[0].strip()) / 100
            result = number * percentage
            e.delete(0, END)
            e.insert(END, str(result))
        else:
            result = eval(expression)
            e.delete(0, END)
            e.insert(END, str(result))
    except Exception as error:
        e.delete(0, END)
        e.insert(END, "Error")

def button_subtract():
    e.insert(END, '-')

def button_multiply():
    e.insert(END, '*')

def button_divide():
    e.insert(END, '/')

def button_percent():
    e.insert(END, '%')

def button_decimal():
    e.insert(END, '.')

button_1 = Button(root, text='1', padx=40, pady=20, command=lambda: button_click('1'))
button_2 = Button(root, text='2', padx=40, pady=20, command=lambda: button_click('2'))
button_3 = Button(root, text='3', padx=40, pady=20, command=lambda: button_click('3'))
button_4 = Button(root, text='4', padx=40, pady=20, command=lambda: button_click('4'))
button_5 = Button(root, text='5', padx=40, pady=20, command=lambda: button_click('5'))
button_6 = Button(root, text='6', padx=40, pady=20, command=lambda: button_click('6'))
button_7 = Button(root, text='7', padx=40, pady=20, command=lambda: button_click('7'))
button_8 = Button(root, text='8', padx=40, pady=20, command=lambda: button_click('8'))
button_9 = Button(root, text='9', padx=40, pady=20, command=lambda: button_click('9'))
button_0 = Button(root, text='0', padx=40, pady=20, command=lambda: button_click('0'))
button_add = Button(root, text='+', padx=39, pady=20, command=button_add)
button_equal = Button(root, text='=', padx=40, pady=20, command=button_equal)
button_clear = Button(root, text='C', padx=40, pady=20, command=button_clear)
button_subtract = Button(root, text='-', padx=40, pady=20, command=button_subtract)
button_multiply = Button(root, text='*', padx=40, pady=20, command=button_multiply)
button_divide = Button(root, text='/', padx=40, pady=20, command=button_divide)
button_percent = Button(root, text="%", padx=40, pady=20, command=button_percent)
button_decimal = Button(root, text=".", padx=40, pady=20, command=button_decimal)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1)

button_multiply.grid(row=6, column=2)
button_divide.grid(row=6, column=1)
button_subtract.grid(row=6, column=0)

button_percent.grid(row=4, column=2)
button_decimal.grid(row=5, column=2)

root.mainloop()