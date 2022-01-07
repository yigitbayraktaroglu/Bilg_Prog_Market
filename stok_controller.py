import sqlite3 as sql
from tkinter import *

def stokTakip():
    veriler = []
    vt = sql.connect('stok.sqlite')
    im = vt.cursor()
    im.execute("SELECT * FROM urunler")
    for veri in im:
        if 5>veri[3]:
            veriler.append(veri)
    vt.commit()
    vt.close()
    return veriler



def stokTakip_gui():
    root = Tk()
    root.title("Stok Kontrol")

    x=stokTakip()
    lbl2 = Label(root, text="Stok Uyarısı")
    lbl2.pack()

    for i in x:
        lbl1 = Label(root, text=i)
        lbl1.pack()
    btn = Button(root, text="Kapat", command=root.destroy)
    btn.pack()

    root.mainloop()
