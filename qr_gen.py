#import Library

from datetime import date, time 
import qrcode
from PIL import Image


date_qr = date.today()
time_qr = date_qr.strftime("%d/%m/%Y %H:%M:%S")

#Generate QR code

name = input("Name of the product: ")
batch_no = input("Batch No. of the product: ")
release = input("Release No: ")
code = int(input('Code of Product: '))

qr = qrcode.QRCode (
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

data = f'''
  Name : {name} \n
  Batch Number : {batch_no} \n
  Release Number : {release} \n
  Code of Product : {code} \n
  Time : {time_qr} 
'''

qr.add_data(data)

img = qr.make_image(fill_color="white", back_color="black")
img.save("qr.png")
