import qrcode
#aca deberas poner la url que deses que se convierta en QR
url="https://google.com"
qr=qrcode.QRCode(version=1,box_size=10,border=5)
qr.add_data(url)
qr.make(fit=True)
img=qr.make_image(fill='black',back_color='white')
#Y te recomiendo aca vas cambiando el numerito de la imagen
img.save('qrcode001.png')
