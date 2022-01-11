import sqlite3 as sql
import barkod_olustur
import user_db
import datetime
an=datetime.datetime.now()
liste = []
user = []


def data(used_codes):
    vt = sql.connect('stok.sqlite')
    im = vt.cursor()
    for i in used_codes:
        im.execute("SELECT * FROM urunler WHERE URUN_NO=?", (i,))
        liste.append(im.fetchall())
        if i > 1000:
            user.append(i)
            liste.remove(i)
    fis(liste)
    stokislemi(liste)
    vt.commit()
    vt.close()


def fis(liste):
    f = open(an+".txt", "w")
    f.write("Toplam Fiyat:" + fiyatislemi(liste) + "\n")
    for i in liste:
        str1 = str(i)
        txt = str1.split(",")
        f.write("Urun No:" + txt[0][2:] + " Urun Adı:" + txt[1] +
                " Fiyat:" + txt[2] + " Son Kullanma Tarihi:" + txt[4][0:13] + "\n")
    f.close()


def stokislemi(liste):
    vt = sql.connect('stok.sqlite')
    im = vt.cursor()
    for i in liste:
        str1 = str(i)
        txt = str1.split(",")
        im.execute("UPDATE urunler SET STOK=STOK-1 WHERE URUN_NO=?", (txt[0][2:],))
    vt.commit()
    vt.close()


def fiyatislemi(liste):
    ucret = 0
    for i in liste:
        str1 = str(i)
        txt = str1.split(",")
        ucret = ucret + int(txt[2])
    user_db.kullaniciPuan(user[0],ucret)
    return str(ucret)


def stokArttir(yeni_stok, urun_no):
    vt = sql.connect('stok.sqlite')
    im = vt.cursor()
    im.execute("UPDATE urunler SET STOK = ? WHERE URUN_NO=?", (yeni_stok, urun_no))
    vt.commit()
    vt.close()


def fiyatArttir(yeni_fiyat, urun_no):
    vt = sql.connect('stok.sqlite')
    im = vt.cursor()
    im.execute("UPDATE urunler SET FIYAT = ? WHERE URUN_NO=?", (yeni_fiyat, urun_no))
    vt.commit()
    vt.close()


def urunOlustur(urun_ad, urun_fiyat, urun_stok, skt):
    vt = sql.connect('stok.sqlite')
    im = vt.cursor()
    urun_no = urunNoOlustur()
    im.execute("""INSERT INTO urunler VALUES (?,?,?,?,?)""", (urun_no, urun_ad, urun_fiyat, urun_stok, skt))
    barkod_olustur.barkod_olustur(urun_no)
    vt.commit()
    vt.close()


def urunNoOlustur():
    vt = sql.connect('stok.sqlite')
    im = vt.cursor()
    im.execute('SELECT max(URUN_NO) FROM urunler')
    max_id = im.fetchone()[0]
    vt.commit()
    vt.close()
    return max_id + 1
