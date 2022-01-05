import user_db as db
from tkinter import *


def user_gui():
    def olustur():
        user_name = e1.get()
        sifre = e2.get()
        db.kullaniciOlustur(user_name, 0, sifre)
        lbl3 = Label(root, text="Kullanici Olusturuldu.")
        lbl3.grid(row=4, column=0)

    root = Tk()
    root.title("Kullanici Islemleri")
    root.geometry("600x300")

    lbl1 = Label(root, text="Kullanici Adi:")
    lbl1.grid(row=0, column=0)

    lbl2 = Label(root, text="Sıfre:")
    lbl2.grid(row=1, column=0)

    e1 = Entry(root)
    e1.grid(row=0, column=1)

    e2 = Entry(root)
    e2.grid(row=1, column=1)

    # button ekleme bölümü
    button1 = Button(root, text="Kullanıcı Olustur", command=olustur)
    button1.grid(row=2, column=0)
    btn = Button(root, text="Kapat", command=root.destroy)
    btn.grid(row=3, column=0)

    root.mainloop()
