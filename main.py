import matplotlib.pyplot as plt

from parsers import parse_drill_set
from plotting import plot_set


def main():
    drill_file = 'drillfiles/2024_song_2.txt'

    file = open(drill_file, 'rt')
    current_text = file.read()
    current_set = parse_drill_set(current_text)
    ax = plot_set(current_set)
    file.close()
    while True:
        file = open(drill_file, 'rt')
        current_text = file.read()
        # if new_text != current_text:
        #     print('New!')
        #     current_text = new_text
        #     current_set = parse_drill_set(8, current_text)
        try:
            current_set = parse_drill_set(current_text)
            ax.clear()
            plot_set(current_set, ax)
            plt.show(block=False)
        except Exception as e:
            print(f'File is currently invalid: {e}')
        plt.pause(.001)
        file.close()


if __name__ == '__main__':
    main()
