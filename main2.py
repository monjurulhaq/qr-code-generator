import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=15,
    border=2,
)
qr.add_data('https://github.com/monjurulhaq/qr-code-generator')
qr.make(fit=True)

img = qr.make_image(fill_color="blue", back_color="white")
img.save("qr-of-main2.png")