## script to generate bulk dataset (fake qr codes)

import os, qrcode
import cv2 as cv
import numpy as np

FOLDER = 'dataset/training/fake'  #for test data use FOLDER='dataset/test/fake'

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
    img = cv.blur(src=img, ksize=(4, 4))   #cv.GaussianBlur(img, (3,3),0) for guassian noise
    img = np.dstack((img,img, img))
    print("Generating QR fake img ")
    cv.imwrite(os.path.join(FOLDER, f"{data}-noise.jpg"), img)

