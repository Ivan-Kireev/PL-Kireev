from tkinter import *
from tkinter import ttk
import tkinter as tk
import requests
import json

#интерфейс
window = Tk()
window.title("Киреев Иван Сергеевич")
tab_conrol = ttk.Notebook(window)

lbl = Label(window, text="Введите имя репозитория:")
lbl.grid(column = 0, row = 0)

entry = Entry(window)
entry.grid(column = 0, row = 1)

rslt = Text(window, width=50, height=20, bg='white', fg='blue', wrap=WORD)
rslt.grid(row = 3)

def GET():
    user = entry.get()
    url1 = f'https://api.github.com/users/{user}'
    user_data = requests.get(url1).json()
    s = user_data

    dict = {
        'company' : s.get('company'),
        'created_at' : s.get('created_at'),
        'email' : s.get('email'),
        'id' : s.get('id'),
        'name' : s.get('name'),
        'url' : s.get('url')
        }
    with open('txt.json', 'w') as file:
        json.dump(dict, file, indent = 4)
#каждые данные с новой строки
    rslt.delete(1.0, END)
    for key, value in dict.items():
        rslt.insert(END, f"{key}: {value}\n")

btn = Button(window, text="Получить данные", command = GET)
btn.grid(column = 0, row = 2)

window.mainloop()