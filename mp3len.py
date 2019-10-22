import os
import re
import argparse
from mutagen.mp3 import MP3


def main():
    parser = argparse.ArgumentParser(
        description='This program is used to calculate the total length of all mp3 files in a directory recursively.')
    parser.add_argument('-d',
                        '--dir', help='Location of your mp3 files or folders containing them')

    args = parser.parse_args()

    if args.dir == None:
        print('Directory argument required.')
        exit()

    mp3_files = []
    total_length = 0

    for root, dirs, files in os.walk(os.path.normpath(args.dir)):
        for file in files:
            if file.endswith('.mp3'):
                total_length += MP3(root + '\\' + file).info.length

    print('Total lenght of mp3 files in this directory is:')
    print(int(total_length), 'seconds or')
    print(int(total_length / 60), 'minutes or')
    print(int(total_length / 3600), 'hours')


if __name__ == '__main__':
    main()
