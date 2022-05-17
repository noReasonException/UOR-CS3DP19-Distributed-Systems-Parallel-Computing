import sys

def emit(key,value):
    print(str(key)+" "+str(value))



def reduce(key,values):
    emit(key,sum([int(x) for x in values]))

hashMap = {}
for line in sys.stdin: # process each line in the file.
    key_value=line.split(" ") # tokenize
    key=key_value[0]
    value=key_value[1]
    if(key in hashMap):
        hashMap[key].append(value)
    else:
        hashMap[key]=[value]


for everyKey in hashMap.keys():
    reduce(everyKey,hashMap[everyKey])







