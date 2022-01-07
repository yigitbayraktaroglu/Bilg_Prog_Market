
from tkinter import *
import barkod
import skt_gui
import user_gui
import stok_gui


def gui():
    root = Tk()
    root.title("Market")
    #root.geometry("600x300")
    main_menu = Frame(root)
    main_menu.grid()
    # button ekleme bölümü
    button1 = Button(main_menu, text="Kullanici Olustur", command=user_gui.user_gui)
    button1.grid(row=0, column=0)
    button2 = Button(main_menu, text="Stok Islemleri", command=stok_gui.stok_gui)
    button2.grid(row=1, column=0)
    button3 = Button(main_menu, text="Satıs", command=barkod.bar_reader)
    button3.grid(row=2, column=0)
    button4 = Button(main_menu, text="Son Kullanma Tarihi Kontrol", command=skt_gui.skt_gui)
    button4.grid(row=3, column=0)
    btn = Button(root, text="Kapat", command=root.destroy,bg="RED")
    btn.grid(row=4, column=0)
    root.mainloop()
