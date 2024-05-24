import tkinter as tk

def click(button_text):
    current_expression = str(entry.get())
    if current_expression == "Ошибка" or current_expression == "на ноль делить нельзя":
        entry.delete(0, tk.END)
        current_expression = ""
    updated_expression = current_expression + str(button_text)
    entry.delete(0, tk.END)
    entry.insert(0, updated_expression)

def clear():
    entry.delete(0, tk.END)

def square():
    try:
        expression = entry.get()
        result = eval(expression) ** 2
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Ошибка")

def evaluate():
    try:
        expression = entry.get()
        if '/0' in expression or '/ 0' in expression:
            raise ZeroDivisionError
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except ZeroDivisionError:
        entry.delete(0, tk.END)
        entry.insert(0, "на ноль делить нельзя")
    except SyntaxError:
        entry.delete(0, tk.END)
        entry.insert(0, "Ошибка")
    except NameError:
        entry.delete(0, tk.END)
        entry.insert(0, "Ошибка")
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Ошибка")

window = tk.Tk()
window.title("Калькулятор")
window.geometry("470x500")  # Увеличиваем размер окна

# Приветственное сообщение
tk.Label(window, text="Добро пожаловать в Калькулятор!", font=('Arial', 20)).grid(row=0, column=0, columnspan=4)

entry = tk.Entry(window, width=30, font=('Arial', 20))
entry.grid(row=1, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    '^2'  # Кнопка возведения в квадрат
]

row_val = 2
col_val = 0

for button in buttons:
    if button == "=":
        tk.Button(window, text=button, width=5, height=2, font=('Arial', 20), command=evaluate).grid(row=row_val, column=col_val)
    elif button == "^2":
        tk.Button(window, text=button, width=5, height=2, font=('Arial', 20), command=square).grid(row=row_val, column=col_val)
    else:
        action = lambda x = button: click(x)
        tk.Button(window, text=button, width=5, height=2, font=('Arial', 20), command=action).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

clear_button = tk.Button(window, text='C', width=5, height=2, font=('Arial', 20), command=clear)
clear_button.grid(row=row_val, column=col_val)

window.mainloop()
