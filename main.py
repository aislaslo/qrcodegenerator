import qrcode
from PIL import Image

data = input("Enter anything to generate a QR: ")

qr = qrcode.QRCode(version=2, box_size=10, border=4)
qr.add_data(data)
qr.make(fit=True)
image = qr.make_image(fill="black", black_color="yellow")

image.save("qr_code.png")