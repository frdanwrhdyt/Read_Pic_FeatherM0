import binascii
import cv2
import numpy as np
import os
import serial

__version__ = 0.1

class Image:
    def __init__(self):
        self.img = []

    def get_img(self, src):
        self.img.append(binascii.a2b_hex(src))
        lenght = len(self.img)
        return lenght

    def show_img(self, con):
        nparr = np.fromstring(self.img[con-1], np.uint8)
        img_decode = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        cv2.imshow('image', img_decode)
        cv2.waitKey()
        
    def save_img(self, con):
        i = 1
        while os.path.exists('img%s.jpg' % i):
            with open('img%s.jpg' % i, 'wd') as file:
                file.write(self.img[con-1])
                file.close()

class Command:
    def __init__(self, baud, port) -> None:
        self.serial = serial.Serial(baudrate=baud, port=port)

    def send_command(self, com):
        self.com = com
        ser = self.serial
        print('[PROCESSING]...')
        com = bytes(self.com, 'utf-8')
        ser.write(com)
        print('[DONE]')
        input('Press [ENTER] to continue')
        os.system('cls')

    def read_image(self):
        ser = self.serial
        ser.write(self.com)
        ser_byte = ser.readline()

        decode_bytes = ser_byte[0:len(ser_byte)]
        img = Image.get_img(src = decode_bytes)
        return img
                
    def show_image(self,picture):
        Image.show_img(picture)

    def save_image(self, picture):
        Image.save_img(picture)