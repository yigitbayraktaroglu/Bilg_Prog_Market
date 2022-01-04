import datetime
import sqlite3 as sql
an = datetime.datetime.now()


def uyar(veri):
    veriler=[]
    veriler.append(veri)
def skt():
    veriler = []
    vt = sql.connect('stok.sqlite')
    im = vt.cursor()
    im.execute("SELECT * FROM urunler")
    for veri in im:
        tarih=veri[4]
        x=tarih.split(".")
        if int(x[2]) < an.year:
            veriler.append(veri)
        elif int(x[2]) == an.year:
            if int(x[1]) < an.month:
                veriler.append(veri)
            elif int(x[1]) == an.month:
                if int(x[0]) < an.day:
                    veriler.append(veri)
                elif int(x[0]) == an.day:
                    veriler.append(veri)
                else:
                    pass
            else:
                pass
        else:
            pass
    return veriler
    vt.commit()
    vt.close()

