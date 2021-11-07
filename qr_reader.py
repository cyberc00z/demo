from pyzbar import pyzbar
import cv2 as cv

def _decode(img):
    """
    """
    img = cv.imread(img)
    result = pyzbar.decode(img)
    for i in result:
        print(i.data.result("utf-8"))

img = input('Enter the qr code path : ')
_decode(img)
