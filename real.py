## script to generate bulk dataset (real qr codes)

import os, qrcode
import cv2 as cv
import numpy as np

FOLDER = 'dataset/training/real'  #for test data use FOLDER='dataset/test/real'

if not os.path.isdir(FOLDER):
    os.mkdir(FOLDER)
    
for data in np.random.choice(np.arange(1000,10000), size=2500, replace=False):
    qr = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_M,
    box_size=10,
    border=4
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color='black', back_color='white')
    img = np.float32(np.asarray(img))*255
    img = np.dstack((img,img, img))
    print("Generating QR codes img ")
    cv.imwrite(os.path.join(FOLDER, f"{data}.jpg"), img)

