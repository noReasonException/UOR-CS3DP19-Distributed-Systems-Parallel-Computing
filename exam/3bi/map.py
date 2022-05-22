import sys


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


def emitIntermidiate(key, value):
    """
    emits Key-Value pairs to the reducer
    :param key: key to be emitted
    :param value: value to be emitted
    :return: None
    """
    print(str(key) + " " + str(value))
    return None


for line in sys.stdin:  # Process each line in the file.
    uni, subject, studentsNo, femNo, malNo = filterStdin(line).split(" ")  # split each line into tokens
    emitIntermidiate(uni, studentsNo)  # Emit university - studentsNo pairs
