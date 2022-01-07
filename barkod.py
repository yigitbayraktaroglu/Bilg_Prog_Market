import db
import cv2
from pyzbar.pyzbar import decode
import time


def bar_reader():
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)
    used_codes = []

    while cap.isOpened():
        success, frame = cap.read()
        cv2.imshow('Kapamak icin Q tusuna basiniz.', frame)
        cv2.waitKey(1)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        for code in decode(frame):
            if code.data.decode('utf-8') not in used_codes:
                print("Approved.You can enter.")
                print(code.data.decode('utf-8'))
                used_codes.append(code.data.decode('utf-8'))
                time.sleep(1)
            elif code.data.decode('utf-8') in used_codes:
                print('Sorry,this code has been already used!')
                time.sleep(1)
            else:
                pass
    cv2.destroyAllWindows()
    db.data(used_codes)

