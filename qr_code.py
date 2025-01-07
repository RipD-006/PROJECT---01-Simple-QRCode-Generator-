# [PYTHON PROJECT] : Simple QR Code Generator

import qrcode as qr

# make() function can be used only after importing the module [i.e. qrcode] and allows one to generate a QR Code
img = qr.make("https://www.linkedin.com/in/ripan-das-375b33286")

# save() function can be used only after importing the module [i.e. qrcode] and allows one to save the generated qr code as an image file
img.save("Generated_QR.png")

# OUTPUT : When this program gets executed a QR Code gets generated and is saved within the same file directory as an image file - further this Unique Code can be scanned through valid devices in order to access the respective URL that has been mentioned within the make("__URL__") function.