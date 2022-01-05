from tkinter import *
import skt_controller


def skt_gui():
    root = Tk()
    root.title("Son Kullanma Tarihi Kontrol")
    root.geometry("600x300")
    skt = skt_controller.skt()
    lbl2 = Label(root, text="Son Kullanma Tarihi gecen urunler")
    lbl2.pack()

    for i in skt:
        lbl1 = Label(root, text=i)
        lbl1.pack()
    btn = Button(root, text="Kapat", command=root.destroy)
    btn.pack()

    root.mainloop()
