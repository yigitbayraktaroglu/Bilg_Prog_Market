import sqlite3 as sql


def kullaniciOlustur(user_name, points, sifre):
    vt = sql.connect('kullanici.sqlite')
    im = vt.cursor()
    user_id = useridOlustur()
    im.execute("""INSERT INTO  users VALUES (?,?,?,?)""", (user_id, user_name, points, sifre))
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