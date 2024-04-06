import os, sys
def getMatchIDs(filename):
    reading = open(filename,"r", encoding='utf-8-sig')
    currLine = reading.readline()
    ids = {"-1"}
    while True:
        if currLine == "":
            break
        else:
            id = currLine.split(",")[0]
            id = id.split("(")[1]
            id = id.strip()
            ids.add(id)
        currLine = reading.readline()
    reading.close()
    return ids
def removeUnneeded(path,filename):
    dir = os.listdir(path)
    foundSet = getMatchIDs(filename)
    for file in dir: 
        num = file.split(".")[0]
        if num not in foundSet and "remove" not in file and "Match" not in file:
            os.remove(file)
removeUnneeded(".","Match.csv")
