import time
import traceback
from typing import TextIO

import matplotlib.pyplot as plt
import os

from parsers import parse_drill_file
from plotting import plot_set
from drill_objects import DrillFormatException


def main():
    drill_file = 'drillfiles/2024_song_2.txt'

    file = open(drill_file, 'rt')

    plt.ion()
    fig, ax = plt.subplots()

    set_number = 0

    while True:
        file.seek(0)
        text = file.read()
        try:
            current_sets = parse_drill_file(text)

            plot_set(current_sets[set_number], ax)
            time.sleep(.01)
        except DrillFormatException as e:
            print(f'File is currently invalid: {e}')
            continue
        except Exception as e:
            print(traceback.print_exc())
            print(e)
            continue

        cmd, *args = input('Command: ').split(' ')

        if not cmd or cmd == 'update':
            continue
        elif cmd == 'set':
            new_number = int(args[0])
            if new_number < len(current_sets):
                set_number = new_number
            else:
                print('number too big')

        else:
            print('Invalid command')


if __name__ == '__main__':
    main()
