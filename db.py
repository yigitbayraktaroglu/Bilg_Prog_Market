
import sqlite3 as sql
deneme=[]


def data(used_codes):
    vt = sql.connect('stok.sqlite')
    im = vt.cursor()
    for i in used_codes:
        im.execute("SELECT * FROM urunler WHERE URUN_NO=?", (i,))
        deneme.append(im.fetchall())
        fis(deneme)
    vt.commit()
    vt.close()

def fis(deneme):
    f=open("deneme.txt","w")
    str1=' '.join(map(str, deneme))
    f.write(str1)
    f.close()

def stokislemi():
    vt = sql.connect('stok.sqlite')
    im = vt.cursor()

    vt.commit()
    vt.close()
    pass


def fiyatislemi():
    vt = sql.connect('stok.sqlite')
    im = vt.cursor()

    vt.commit()
    vt.close()
    pass


def stokArttir(yeni_stok,urun_no):
    vt = sql.connect('stok.sqlite')
    im = vt.cursor()
    im.execute("UPDATE urunler SET STOK = ? WHERE URUN_NO=?",(yeni_stok,urun_no))

    vt.commit()
    vt.close()



def fiyatArttır(yeni_fiyat,urun_no):
    vt = sql.connect('stok.sqlite')
    im = vt.cursor()
    im.execute("UPDATE urunler SET FIYAT = ? WHERE URUN_NO=?", (yeni_fiyat, urun_no))
    vt.commit()
    vt.close()


def urunOlustur(urun_ad,urun_fiyat,urun_stok,skt):
    vt = sql.connect('stok.sqlite')
    im=vt.cursor()
    urun_no=urunNoOlustur()
    im.execute("""INSERT INTO urunler VALUES (?,?,?,?,?)""",(urun_no,urun_ad,urun_fiyat,urun_stok,skt))
    vt.commit()
    vt.close()


def urunNoOlustur():
    vt = sql.connect('stok.sqlite')
    im = vt.cursor()
    im.execute('SELECT max(URUN_NO) FROM urunler')
    max_id = im.fetchone()[0]
    vt.commit()
    vt.close()
    return max_id+1



