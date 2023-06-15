from tkinter import *
from tkinter import ttk
import math

# Функции для операций
def add():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    result = num1 + num2
    label_result.config(text="Результат: " + str(result))

def subtract():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    result = num1 - num2
    label_result.config(text="Результат: " + str(result))

def multiply():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    result = num1 * num2
    label_result.config(text="Результат: " + str(result))

def divide():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    result = num1 / num2
    label_result.config(text="Результат: " + str(result))

def sin():
    num = float(entry_num1.get())
    result = math.sin(math.radians(num))
    label_result.config(text="Результат: " + str(result))

def cos():
    num = float(entry_num1.get())
    result = math.cos(math.radians(num))
    label_result.config(text="Результат: " + str(result))

def tan():
    num = float(entry_num1.get())
    result = math.tan(math.radians(num))
    label_result.config(text="Результат: " + str(result))

def cot():
    num = float(entry_num1.get())
    result = 1 / math.tan(math.radians(num))
    label_result.config(text="Результат: " + str(result))

# Создаем графический интерфейс
root = Tk()
root.title("Калькулятор")
root.geometry("360x240")

# Применяем стиль материального дизайна
style = ttk.Style()
style.theme_use('clam')

# Устанавливаем размер шрифта для кнопок
style.configure('TButton', font=('Roboto', 12))

# Устанавливаем размер шрифта для полей ввода
style.configure('TEntry', font=('Roboto', 12))

# Создаем метки и поля ввода для чисел
label_num1 = Label(root, text="Число:")
label_num1.grid(row=0, column=0)
entry_num1 = ttk.Entry(root)
entry_num1.grid(row=0, column=1)

label_num2 = Label(root, text="Второе число:")
label_num2.grid(row=1, column=0)
entry_num2 = ttk.Entry(root)
entry_num2.grid(row=1, column=1)

# Создаем кнопки для операций
button_add = ttk.Button(root, text="+", command=add)
button_add.grid(row=2, column=0, sticky="nsew")

button_subtract = ttk.Button(root, text="-", command=subtract)
button_subtract.grid(row=2, column=1, sticky="nsew")

button_multiply = ttk.Button(root, text="*", command=multiply)
button_multiply.grid(row=3, column=0, sticky="nsew")

button_divide = ttk.Button(root, text="/", command=divide)
button_divide.grid(row=3, column=1, sticky="nsew")

button_sin = ttk.Button(root, text="sin", command=sin)
button_sin.grid(row=4, column=0, sticky="nsew")

button_cos = ttk.Button(root, text="cos", command=cos)
button_cos.grid(row=4, column=1, sticky="nsew")

button_tan = ttk.Button(root, text="tg", command=tan)
button_tan.grid(row=5, column=0, sticky="nsew")

button_cot = ttk.Button(root, text="ctg", command=cot)
button_cot.grid(row=5, column=1, sticky="nsew")

# Метка для вывода результата
label_result = Label(root, text="Результат:")
label_result.grid(row=6, columnspan=2)

# Задаем вес для кнопок и ячеек, чтобы они растягивались
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)
root.grid_rowconfigure(5, weight=1)

# Запускаем главный цикл обработки событий
root.mainloop()
