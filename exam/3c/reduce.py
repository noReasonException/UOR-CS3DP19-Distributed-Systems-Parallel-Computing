import sys


def emit(key, value):
    print(str(key) + " " + str(value))


def percentageReducer(key, values):
    femTotal = sum([int(x[0]) for x in values])
    studTotal = sum([int(x[1]) for x in values])
    emit(key, femTotal/studTotal)



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
    key_values = filterStdin(line).split(" ")  # key-value tokens
    key = key_values[0]
    femNo,total = key_values[1:len(key_values)]
    # if key not found in hashmap, initialize key and add value
    # otherwise, just add value to the value-list under a specific key
    if key in hashMap:
        hashMap[key].append([femNo,total])
    else:
        hashMap[key] = [[femNo,total]]

for everyKey in hashMap.keys():
    percentageReducer(everyKey, hashMap[everyKey])

