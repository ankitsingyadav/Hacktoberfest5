# install library first by running this in terminal:
# pip install qrcode

import qrcode

# Take input from user
data = input("Enter text or link to generate QR code: ")

# Create QR code
qr = qrcode.make(data)

# Save QR code as an image file
qr.save("myqrcode.png")

print("✅ QR Code generated successfully and saved as 'myqrcode.png'")
