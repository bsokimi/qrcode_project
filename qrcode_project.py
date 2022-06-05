
import qrcode

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

datastr = "input_data"
qr.add_data(datastr)
qr.make(fit=True)

img = qr.make_image(back_color=(255, 195, 235), fill_color=(55, 95, 35))
img.save("QRCode.png")