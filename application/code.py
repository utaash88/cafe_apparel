import qrcode
img = qrcode.make('Some data here')
img.save("qrcode.png")