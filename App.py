import tkinter as tk
from tkinter import ttk
from tkinter import *
import webbrowser
import requests
from bs4 import BeautifulSoup
from tkinter import messagebox
from pyowm import OWM



# Создание приложения
app = tk.Tk()
app.title('Поисковая система')
app.geometry('640x280')
app.configure(background='#2F4F4F')

# Создание текстовой надписи
search_label = ttk.Label(app, text='Поиск', font='verdana 13 bold', background='#2F4F4F')
search_label.grid(row=0, column=0)

# Создание текстового поля для ввода текста
text_field = ttk.Entry(app, width=50)
text_field.grid(row=0, column=1)
# Переменная для выбора поисковой системы (по умолчанию одна)
seacrh_engine = StringVar()
seacrh_engine.set('google')

# Поиск информации в браузере
def search():
    if text_field.get().strip() != '':
        if seacrh_engine.get() == 'google':
            webbrowser.open('https://www.google.com/search?q=' + text_field.get())


def searchBtn():
    search()


def enterBtn(event):
    search()

btn_search = ttk.Button(app, text='Найти', width=7, command=searchBtn)
btn_search.grid(row=0, column=2)

text_field.bind('<Return>', enterBtn)

radio_google = ttk.Radiobutton(app, text='Google', value='google', variable=seacrh_engine)
radio_google.grid(row=1, column=1, sticky=W)


app.wm_attributes('-topmost', True)

text_field.focus()

weather2_label = ttk.Label(app, text="Укажите название города:", font="Consolas 12 bold", background='#2F4F4F')
weather2_label.grid(row=2, column=3, sticky=W)
owm = OWM('your_api-key')
a = ttk.Entry(app, width=35)
a.grid(row=3, column=3)


def temp():
    b = str(a.get())
    search_w = f"Погода в {b}"

    url = f"https://www.google.com/search?&q={search_w}"

    r = requests.get(url)
    s = BeautifulSoup(r.text, "html.parser")

    update = s.find("div", class_="BNeawe").text

    if b == 'developer':
        dev()
        a.delete(first=0, last=10000)

    c = messagebox.showinfo("Прогноз погоды", "В городе " + b + " температура " + update)

    a.delete(first=0, last=10000)


def dev():
    print("Введите название города/страны:")
    place = input()
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(place)
    w = observation.weather
    temp = w.temperature('celsius')['temp']
    print("Температура " + str(temp))
    print(w)


button_w = ttk.Button(app, text="Узнать температуру", command=temp, width=18)
button_w.grid(row=4, column=3)




# Создание функции которая не позволяет закрываться приложению
app.mainloop()