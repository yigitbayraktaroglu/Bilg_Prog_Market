import sqlite3 as sql
import cv2
from pyzbar.pyzbar import decode
import time
vt = sql.connect('kitaplar.sqlite')
im = vt.cursor()
cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
used_codes=[]
camera=True
while camera==True:
    success, frame =cap.read()
    for code in decode(frame):
        if code.data.decode('utf-8') not in used_codes:
            print("Approved.You can enter.")
            print(code.data.decode('utf-8'))
            used_codes.append(code.data.decode('utf-8'))
            time.sleep(1)
            im.execute("SELECT * FROM kitaplar WHERE Yazar=?",(used_codes[0],))
            print("1",im.fetchall())
        elif code.data.decode('utf-8') in used_codes:
            print('Sorry,this vode has been already used!')
            time.sleep(1)
        else:
            pass
    cv2.imshow('Test',frame)
    cv2.waitKey(1)