import sys


def emit(key, value):
    print(str(key) + " " + str(value))


def sumReducer(key, values):
    emit(key, sum([int(x) for x in values]))

def filterStdin(line):
    """
    Filters new-line characters from the end of each line
    :param line: an individual line as a string
    example : Bristol Chemistry 134 73 61
    :return: The line without the new line ('\n') character
    """
    filteredLine = line
    if '\n' in line:
        filteredLine = line[0:len(line) - 1]
    return filteredLine

"""
We use a dictionary, to keep all the values of a specific key
"""
hashMap = {}
for line in sys.stdin:  # process each line in the file.
    key,value = filterStdin(line).split(" ")  # key-value tokens
    # if key not found in hashmap, initialize key and add value
    # otherwise, just add value to the value-list under a specific key
    if key in hashMap:
        hashMap[key].append(value)
    else:
        hashMap[key] = [value]

for everyKey in hashMap.keys():
    sumReducer(everyKey, hashMap[everyKey])
