from tkinter import *
from tkinter.ttk import Combobox
from tkinter import ttk, filedialog, messagebox, Radiobutton, Menu

#создание окна
window = Tk()
window.title("Киреев Иван Сергеевич")
window.geometry('650x400')
tab_control = ttk.Notebook(window)

#калькулятор
tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Калькулятор')
tab_control.pack(expand=1, fill='both')

txt = Entry(tab1, width = 10, fg = 'white', bg = 'blue')
txt.grid(column = 0, row = 0)
combo = Combobox(tab1)
combo['values'] = ('*', '/', '-', '+')
combo.current(1)
combo.grid(column = 1, row = 0)
txt1 = Entry(tab1, width = 10, fg = 'white', bg = 'blue')
txt1.grid(column = 3, row = 0)

#рабочее пространство калькулятора

def vivod(d):
    lbl = Label(tab1, fg = 'white', bg = 'red')
    lbl.configure(text = d)
    lbl.grid(column = 5, row = 0)
def calcul():
    a = txt.get()
    b = txt1.get()
    c = combo.get()
    if c == '/':
        if b == '0':
            messagebox.showerror('error', 'нельзя делить на 0')
        d = float(a)/float(b)
        vivod(d)
    if c == '*':
        d = float(a) * float(b)
        vivod(d)
    if c == '-':
        d = float(a) - float(b)
        vivod(d)
    if c == '+':
        d = float(a) + float(b)
        vivod(d)

# кнопка равенства

btn = Button(tab1, text = '=', command = calcul, fg = 'white', bg = 'blue')
btn.grid(column = 4, row = 0)

#вторая вкладка
def clicked1():
    messagebox.showinfo('information', 'вы выбрали 1 вариант')
def clicked2():
    messagebox.showinfo('information', 'вы выбрали 2 вариант')
def clicked3():
    messagebox.showinfo('information', 'вы выбрали 3 вариант')

tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text = 'выбор варианта')

rad1 = Radiobutton(tab2, text = 'Первый', value = 1, command = clicked1)
rad2 = Radiobutton(tab2, text = 'Второй', value = 2, command = clicked2)
rad3 = Radiobutton(tab2, text = 'Третий', value = 3, command = clicked3)
rad1.grid(column = 1, row = 0)
rad2.grid(column = 1, row = 1)
rad3.grid(column = 1, row = 2)

#Третья вкладка
tab3 = ttk.Frame(tab_control)
tab_control.add(tab3, text = 'работа с текстом')

def clickedfile():
    file = filedialog.askopenfilename(filetypes = [("Text files", "*.txt")])
    if file:
        with open(file, 'r') as file:
            s = file.read()
            text.delete(1.0, END)
            text.insert(END, s)

menu = Menu(window)
new_item = Menu(menu, tearoff = 0)
new_item.add_command(label = 'Новый файл', command = clickedfile)
menu.add_cascade(label = 'Файл', menu = new_item)
window.config(menu = menu)

text = Text(tab3, width = 90, height = 20, bg = 'white', fg = 'black', wrap = WORD)
text.pack()


window.mainloop()
