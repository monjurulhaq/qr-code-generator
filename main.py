import qrcode as qr
img= qr.make("https://github.com/monjurulhaq")
img.save("qr-of-main.png")