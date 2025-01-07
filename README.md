# [PROJECT-01] Simple QRCode Generator:
This Python project is designed to generate QR codes based on user input. A QR code (Quick Response Code) is a type of matrix barcode that stores information such as URLs, text, contact details, and more. The application takes a string and converts it into a QR code image, which can then be saved or displayed.

# Features:
1) INPUT FLEXIBILITY: Accepts any string input, such as URLs, plain text, or contact information, and generates the corresponding QR Code.
2) SAVE AS IMAGE: Users can save the generated QR Code as an image file (i.e. PNG, JPEG, etc).
3) DISPLAY OPTION: Displays the QR Code in a graphical  window for immediate scanning.
4) SIMPLE INTERFACE: The project provides both command-line and GUI-based interfaces for ease of use.

# Required Libraries & Dependencies :
qrcode: The core library to generate the QR codes.

pillow: A Python Imaging Library (PIL) fork used for handling image operations.

# Installation:
    pip install qrcode[pil]
