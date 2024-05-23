import tkinter as tk

def click(button_text):
    current_expression = str(entry.get())
    updated_expression = current_expression + str(button_text)
    entry.delete(0, tk.END)
    entry.insert(0, updated_expression)

def clear():
    entry.delete(0, tk.END)

def evaluate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Ошибка")

window = tk.Tk()
window.title("Калькулятор")
window.geometry("470x500")  # Увеличиваем размер окна

entry = tk.Entry(window, width=30, font=('Arial', 20))
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    action = lambda x = button: click(x)
    if button == "=":
        tk.Button(window, text=button, width=5, height=2, font=('Arial', 20), command=evaluate).grid(row=row_val, column=col_val)
    else:
        tk.Button(window, text=button, width=5, height=2, font=('Arial', 20), command=action).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

clear_button = tk.Button(window, text='C', width=5, height=2, font=('Arial', 20), command=clear)
clear_button.grid(row=row_val, column=col_val)

window.mainloop()
