
from tkinter import *

import barcode
import db


from tkinter import messagebox

def gui():
    pencere = Tk()

    pencere.title("Market")
    pencere.geometry("600x300")

    uygulama = Frame(pencere)
    uygulama.grid()

    # button ekleme bölümü
    button1 = Button(uygulama, text=" KAPAT ", width=50, height=5,command=db.stokArttir(25,1001))
    button1.grid(padx=110, pady=80)

    pencere.mainloop()
gui()
