import qrcode

img = qrcode.make("https://qr-code-gfqi.onrender.com/")
img.save("shop_qr.png")