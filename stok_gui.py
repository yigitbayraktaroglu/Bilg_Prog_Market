import db
from tkinter import *
def stok_gui():
    def urun_olustur():
        def olustur():
            urun_ad = e1.get()
            urun_fiyat = e2.get()
            urun_stok = e3.get()
            skt = e4.get()
            db.urunOlustur(urun_ad, urun_fiyat, urun_stok, skt)
            lbl3 = Label(root, text="Urun Olusturuldu.")
            lbl3.grid(row=6, column=0)
        root = Tk()
        root.title("Urun Islemleri")
        root.geometry("300x140")

        lbl1=Label(root,text="Urun Adi:")
        lbl1.grid(row=0,column=0)

        lbl2=Label(root,text="Fiyat:")
        lbl2.grid(row=1,column=0)

        lbl3 = Label(root, text="Stok:")
        lbl3.grid(row=2, column=0)

        lbl4 = Label(root, text="Son Kullanma Tarihi:")
        lbl4.grid(row=3, column=0)

        e1= Entry(root)
        e1.grid(row=0, column=1)

        e2=Entry(root)
        e2.grid(row=1,column=1)

        e3 = Entry(root)
        e3.grid(row=2, column=1)

        e4 = Entry(root)
        e4.grid(row=3, column=1)

        # button ekleme bölümü
        button1 = Button(root, text="Urun Ekle",command=olustur)
        button1.grid(row=4, column=0)
        btn = Button(root, text="Kapat", command=root.destroy)
        btn.grid(row=5,column=0)
        root.mainloop()


    def fiyat_gunc():
        def guncelle():
            urun_no=e1.get()
            urun_fiyat = e2.get()
            db.fiyatArttır(urun_fiyat,urun_no)
            lbl3 = Label(root, text="Fiyat Guncellendi.")
            lbl3.grid(row=4, column=0)

        root = Tk()
        root.title("Urun Islemleri")
        root.geometry("300x140")

        lbl1 = Label(root, text="Urun No:")
        lbl1.grid(row=0, column=0)

        lbl2 = Label(root, text="Fiyat:")
        lbl2.grid(row=1, column=0)

        e1 = Entry(root)
        e1.grid(row=0, column=1)

        e2 = Entry(root)
        e2.grid(row=1, column=1)
        # button ekleme bölümü
        button1 = Button(root, text="Fiyat Guncelle", command=guncelle)
        button1.grid(row=2, column=0)
        btn = Button(root, text="Kapat", command=root.destroy)
        btn.grid(row=3, column=0)
        root.mainloop()


    def stok_gunc():
        def guncelle():
            urun_no = e1.get()
            yeni_stok = e2.get()
            db.stokArttir(yeni_stok,urun_no)
            lbl3 = Label(root, text="Fiyat Guncellendi.")
            lbl3.grid(row=4, column=0)

        root = Tk()
        root.title("Urun Islemleri")
        root.geometry("300x140")

        lbl1 = Label(root, text="Urun No:")
        lbl1.grid(row=0, column=0)

        lbl2 = Label(root, text="Yeni Stok Adedi:")
        lbl2.grid(row=1, column=0)

        e1 = Entry(root)
        e1.grid(row=0, column=1)

        e2 = Entry(root)
        e2.grid(row=1, column=1)
        # button ekleme bölümü
        button1 = Button(root, text="Fiyat Guncelle", command=guncelle)
        button1.grid(row=2, column=0)
        btn = Button(root, text="Kapat", command=root.destroy)
        btn.grid(row=3, column=0)
        root.mainloop()


    root=Tk()
    root.title("Stok Islemleri")
    root.geometry("600x300")
    btn1=Button(root,text="Urun olustur.",command=urun_olustur)
    btn1.grid(row=0,column=0)
    btn2 = Button(root, text="Fiyat Guncelle.", command=fiyat_gunc)
    btn2.grid(row=1, column=0)
    btn3 = Button(root, text="Stok Guncelle.", command=stok_gunc)
    btn3.grid(row=2, column=0)
    btn = Button(root, text="Kapat", command=root.destroy)
    btn.grid(row=3, column=0)
    root.mainloop()

