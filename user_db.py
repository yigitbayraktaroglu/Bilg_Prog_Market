import sqlite3 as sql
import barkod_olustur


def kullaniciOlustur(user_name, points, sifre):
    vt = sql.connect('kullanici.sqlite')
    im = vt.cursor()
    user_id = useridOlustur()
    im.execute("""INSERT INTO  users VALUES (?,?,?,?)""", (user_id, user_name, points, sifre))
    barkod_olustur.barkod_olustur(user_id)
    vt.commit()
    vt.close()

def kullaniciPuan(id,ucret):
    vt = sql.connect('kullanici.sqlite')
    im = vt.cursor()
    puan=(ucret//100)*5
    im.execute("UPDATE users SET POINTS=POINTS+? WHERE USER_ID=?", (puan, id))
    vt.commit()
    vt.close()


def useridOlustur():
    vt = sql.connect('kullanici.sqlite')
    im = vt.cursor()
    im.execute('SELECT max(USER_ID) FROM users')
    max_id = im.fetchone()[0]
    vt.commit()
    vt.close()
    return max_id + 1
