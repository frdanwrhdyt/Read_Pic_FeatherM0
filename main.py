import serial
from src.image import Command
import os
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Processing to control camera')
    parser.add_argument('-P', metavar = 'port', type=str, help='\tPort of the MCU', required=True)
    parser.add_argument('-B', metavar='baudrate', type=int, help='\tBaudrate of the MCU', default=9800)
    args = parser.parse_args()

    ser = Command(baud=args.B, port=args.P)
    while True:
        print('Commands :\n1\tTake a picture\n2\tGet data from Feather M0\n3\tDelete all memory\n')
        x = int(input('[1/2/3] : '))
        if x == 1 or x == 3 :
            
            ser.send_command(com=x)
        elif x == 2:
            ser.send_command(com=x)
            pic = ser.read_image()
            print('Lots of pictures : ', pic)
            pict = int(input('Select a picture'))
            print('Commands :\n1\tShow a picture\n2\tSave a picture\n')
            y = input('[1/2] : ')
            if y == 1:
                ser.show_image(pict)
            elif y == 2:
                ser.save_image(pict)
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



