from __future__ import print_function

try:
    import Image
except ImportError:
    from PIL import Image, ImageGrab
import pytesseract
from os import getcwd
from time import sleep

sleep(1)

ImageGrab.grab().save("temp_screencap.png", "PNG")

pytesseract.pytesseract.tesseract_cmd = getcwd() + r'\Tesseract-OCR\tesseract.exe'

print(pytesseract.image_to_string(Image.open('temp_screencap.png')))
