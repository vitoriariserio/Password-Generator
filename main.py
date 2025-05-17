import random
from tkinter import *
import tkinter as tk


alphanumeric_chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','1','2','3','4','5','6','7','8','9','0']


def createpassword():
    global entrance
    if option_menu.get().isdigit():
        quantidade = int(option_menu.get())  
        senha = random.choices(alphanumeric_chars, k=quantidade)
        senha_str = ''.join(senha)
        entrance.delete(0, END)
        entrance.insert(0, senha_str)
    else:
        entrance.delete(0, END)
        entrance.insert(0, "Please choose a valid number!")


Generator = Tk()
Generator.title('Password Generator')
Generator.geometry('500x500')


Label(Generator, text = 'Password Generator',width=20, height=2, font=('Fira code', 22, 'bold')).pack()

entrance = Entry(Generator, font=("Fira code", 14,))
entrance.pack()

Label(Generator, text = 'number of characters', width=20, height=2, font=('Fira code', 15, 'bold')).pack()

option_menu = StringVar()
option_menu.set('number of characters')

dropdown = OptionMenu(Generator, option_menu, '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16')
dropdown.pack(pady=(0, 20))


button_click = Button(Generator, text="Create Password",font=("Fira code", 16),width=20, height=2, bg="#919191",fg="white", command=createpassword)
button_click.pack()

Generator.mainloop()
