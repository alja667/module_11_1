
from PIL import Image
import numpy as np
from PIL import Image, ImageOps, ImageDraw, ImageFont

import sys


def ris (name):
    image = Image.open(name)
    new_size = 200,150
    resized_image = image.resize( new_size)
    resized_image.save("name1.jpg")
    resized_image.save("ris.png")
    image.close()

def titul(name, text):
    tatras = Image.open(name)
    idraw = ImageDraw.Draw(tatras)
    font = ImageFont.truetype("arial.ttf", size=12)
    idraw.text((30, 5), text, font=font, fill ='black')
    tatras.save('name2.png')


ris("ris.jpg")
titul("ris.png", "Для тебя!!!")


img = Image.new('RGBA', (300, 200), 'blue')
img.save('rectangle.png')
tatras = Image.open("rectangle.png")

idraw = ImageDraw.Draw(tatras)
text = "Здрвствуйте!!! \n Вам большой привет!"
font = ImageFont.truetype("arial.ttf", size=24)
idraw.text((10, 10), text, font=font, fill ='black')
tatras.save('rectangle.png')