import qrcode
wl = 'https://thisisnotajumpscare.com/'
qr = qrcode.QRCode(version=1, box_size=5, border=5)
qr.add_data(wl)
qr.make()
img = qr.make_image(fill_color='black', back_color='white')
img.save('not a jumpscare.png')