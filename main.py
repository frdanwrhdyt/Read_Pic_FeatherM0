import serial
from src.image import Command
import os
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Processing to control camera')
    parser.add_argument('-P', metavar = 'port', type=str, help='\tPort of the MCU', required=True)
    parser.add_argument('-B', metavar='baudrate', type=int, help='\tBaudrate of the MCU', default=9800)
    args = parser.parse_args()

    ser = serial.Serial(port=args.P, baudrate=args.B)
    while True:
        print('Commands :\n1\tTake a picture\n2\tGet data from Feather M0\n3\tDelete all memory\n')
        x = int(input('[1/2/3] : '))
        if x == 1 or x == 3 :
            COM = Command(com = x, s=ser)
            COM.send_command()
        elif x == 2:
            COM = Command(com=x, s=ser)
            COM = COM.read_image()
            print('Lots of pictures : ', COM)
            picture = int(input('Select a picture'))
            print('Commands :\n1\tShow a picture\n2\tSave a picture\n')
            y = input('[1/2] : ')
            if y == 1:
                COM.show_image(picture)
            elif y == 2:
                COM.save_image(picture)
            else:
                print('Command no existing')
                input('Press [ENTER] to continue')
                os.system('cls')
                continue
        else:
            print('Command no existing')
            input('Press [ENTER] to continue')
            os.system('cls')
            continue



