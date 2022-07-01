# Задание: реализовать модификацию изображения
# генерируемого QR-кода: раскрасить фрагменты изображения в
# несколько случайно определяемых цветов.



import pyqrcode
import random


red = random.randrange(256)
green = random.randrange(256)
blue = random.randrange(256)
data = pyqrcode.create(input("Введите текст: "))
data.png("qr.png", scale=7, module_color=[red, green, blue, 128],
         background=[red, green, blue])
