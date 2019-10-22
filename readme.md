# Mp3len

Combines total length of all mp3 files in a given directory and sub-directories.

## Prerequisites

```
Python 3.7.2
Mutagen 1.42.0
```

## Usage

From the command line run the program with either '-d' or '--dir' and give it a directory in quotes.

```
python mp3len.py -d 'c:\my_mp3_dir'
```

### Notes

Max depth is not currently implemented so running it in system root is not ideal.
