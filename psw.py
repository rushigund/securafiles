from random import random
from math import floor
from os import path, remove
import schedule
import time
import qrcode
data = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

leng = len(data)


def createpass():
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5

    )
    otp = ""
    if path.exists("psw.txt"):
        remove("psw.txt")
    f = open("psw.txt", "w+")
    for j in range(1, 20):
        for i in range(16):
            otp += data[floor(random() * leng)]

        #print(otp + "\n")
        f.write(otp + "\n")
        otp = ""

    f.close()

    if path.exists("psw.png"):
        remove("psw.png")

    with open('psw.txt', 'r') as g:
        p = g.read().rstrip('\n')

    qr.add_data(p)
    qr.make(fit=True)
    img = qr.make_image(fill="black", back_color="white")
    img.save("psw.png")
    g.close()


createpass()

#schedule.every(7).days.at("10:00").do(createpass)
#while True:
    #schedule.run_pending()
    #time.sleep(1)

