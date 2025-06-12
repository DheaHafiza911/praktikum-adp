import time
import os
from termcolor import colored

lebar_bendera = 30
tinggi_bendera = 10
tinggi_tiang = 20
lebar_tiang = 2

wave_table = [0, 1, 2, 1, 0, -1, -2, -1]
wave_len = len(wave_table)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def draw_flag(frame_num):
    clear()
    for y in range(tinggi_tiang):
        line = colored(' ' * lebar_tiang, 'white', 'on_black')
        if y < tinggi_bendera:
            for x in range(lebar_bendera):
                wave = wave_table[(y + frame_num) % wave_len]           
                pos = x + wave
                if y < tinggi_bendera // 2:
                    if 0 <= pos < lebar_bendera:
                        line += colored(' ', 'white', 'on_red')
                    else:
                        line += ' '
                else:
                    if 0 <= pos < lebar_bendera:
                        line += colored(' ', 'grey', 'on_white')
                    else:
                        line += ' '
            line += ' ' * (lebar_bendera - len(line) + lebar_tiang)
        print(line)

def main():
    frame = 0
    while True:
        draw_flag(frame)
        time.sleep(0.1)
        frame += 1

if __name__ == "__main__":
    main()

