import sys


def emitIntermidiate(key, value):
    print(str(key) + " " + str(value))


for line in sys.stdin:  # process each line in the file.
    words = line.split(" ")  # tokenize
    for every in words:
        filtered = every
        if every[-1] == '\n':
            filtered = every[0:len(every) - 1]
        emitIntermidiate(filtered, 1)
