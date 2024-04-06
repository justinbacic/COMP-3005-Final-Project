#lineups files contain info for Countries, Players, and Positions
import os
def convertPlayers(filename):
    reading = open(filename,"r", encoding='utf-8')
    currLine = reading.readline()
    playersData = []
    while currLine != "":
        while "player_id" not in currLine and currLine != "":
            currLine = reading.readline() 
        player_id = "null"
        player_name = "null"
        nickname = "null"
        jersey_number = "null"
        country_id = "null"
        if currLine =="":
           break
        currPlayer = ""
        player_id = extractVal(currLine)
        currLine = reading.readline()
        player_name = extractVal(currLine)
        currLine = reading.readline()
        nickname = extractVal(currLine)
        currLine = reading.readline()
        jersey_number = extractVal(currLine)
        currLine = reading.readline()
        currLine = reading.readline()
        country_id = extractVal(currLine)
        currPlayer = "("+player_id+", "+player_name+", "+nickname+", "+jersey_number+","+country_id+"),"
        currPlayer = currPlayer.replace('"',"'")
        playersData.append(currPlayer)
        currLine = reading.readline()
    reading.close()
    return playersData
def convertPositions(filename):
    reading = open(filename,"r", encoding='utf-8')
    currLine = reading.readline()
    positionData = []
    match_id = filename.split('.')[0]
    team_id = "null"
    while "team_id" not in currLine:
        currLine = reading.readline()
    team_id = extractVal(currLine)
    currLine = reading.readline()
    while "team_id" not in currLine:
        while "player_id" not in currLine and currLine != "":
            currLine = reading.readline() 
        player_id = "null"
        if currLine =="":
           break
        player_id = extractVal(currLine)
        currLine = reading.readline()
        while "player_id" not in currLine and currLine != "":
            currPosition = ""
            position = "null"
            from_time = "null"
            to_time = "null"
            from_period = "null"
            to_period = "null"
            start_reason = "null"
            end_reason = "null"
            while "position_id" not in currLine and "player_id" not in currLine and currLine!="":
                currLine = reading.readline()
            if currLine =="":
                break
            if "player_id" in currLine:
                break
            currLine = reading.readline()
            position = extractVal(currLine)
            currLine = reading.readline()
            from_time = extractVal(currLine)
            currLine = reading.readline()
            to_time = extractVal(currLine)
            currLine = reading.readline()
            from_period = extractVal(currLine)
            currLine = reading.readline()
            to_period = extractVal(currLine)
            currLine = reading.readline()
            start_reason = extractVal(currLine)
            currLine = reading.readline()
            end_reason = extractVal(currLine)
            currPosition = "("+player_id+", "+team_id+", "+match_id+"," + position+", "+ from_time+", "+to_time+", "+from_period+", "+ to_period+", "+start_reason+", "+end_reason+"),"
            currPosition = currPosition.replace('"',"'")
            positionData.append(currPosition)
            currLine = reading.readline()
    team_id = extractVal(currLine)
    currLine = reading.readline()
    while currLine !="":
        while "player_id" not in currLine and currLine != "":
            currLine = reading.readline() 
        player_id = "null"
        if currLine =="":
           break
        player_id = extractVal(currLine)
        currLine = reading.readline()
        while "player_id" not in currLine and currLine != "":
            currPosition = ""
            position = "null"
            from_time = "null"
            to_time = "null"
            from_period = "null"
            to_period = "null"
            start_reason = "null"
            end_reason = "null"
            while "position_id" not in currLine and "player_id" not in currLine and currLine!="":
                currLine = reading.readline()
            if currLine =="":
                break
            if "player_id" in currLine:
                break
            currLine = reading.readline()
            position = extractVal(currLine)
            currLine = reading.readline()
            from_time = extractVal(currLine)
            currLine = reading.readline()
            to_time = extractVal(currLine)
            currLine = reading.readline()
            from_period = extractVal(currLine)
            currLine = reading.readline()
            to_period = extractVal(currLine)
            currLine = reading.readline()
            start_reason = extractVal(currLine)
            currLine = reading.readline()
            end_reason = extractVal(currLine)
            currPosition = "("+player_id+", "+team_id+", "+match_id+"," + position+", "+ from_time+", "+to_time+", "+from_period+", "+ to_period+", "+start_reason+", "+end_reason+"),"
            currPosition = currPosition.replace('"',"'")
            positionData.append(currPosition)
            currLine = reading.readline()
    reading.close()
    return positionData
def extractVal(str):
    arr = str.split(':',1)
    ret = ""
    if len(arr) > 1:
        ret = arr[1].split(',')[0].strip()
    return ret
def convertCountries(filename):
    reading = open(filename,"r", encoding = 'utf-8')
    countriesFound = {"-1"}
    countryData = []
    currLine = reading.readline()
    while currLine != "":
        while "country" not in currLine and currLine != "":
            currLine = reading.readline() 
        country_id = "null"
        country_name = "null"
        if currLine =="":
           break
        currCountry = ""
        #currLine = reading.readline()
        while "}" not in currLine:
            val = extractVal(currLine)
            if "id" in currLine:
                country_id = val
                currLine = reading.readline()
                country_name = extractVal(currLine)
                continue
            else:
                currLine = reading.readline()
            if(currLine == ""):
                break
        if country_id not in countriesFound and country_id !="null":
            currCountry= "("+country_id+", "+country_name+")"
            currCountry = currCountry.replace('"',"'")
            countryData.append(currCountry)
            countriesFound.add(country_id)
    reading.close()
    return countryData
def callConvert(path,csvDir,type):
    dir = os.listdir(path)
    foundSet = {"-1"}
    for file in dir:
        if os.path.isdir(file):
            curDir = os.getcwd()
            os.chdir("./"+file)
            callConvert(".",csvDir,type)
            os.chdir(curDir)
        elif "a"not in file and"e"not in file and "u"not in file and "i"not in file:
            if type == "PO":
                writeOut(convertPositions(file),csvDir,type)
            if type == "P":
                writeOut(convertPlayers(file),csvDir,type)
            if type == "C":
                writeOut(convertCountries(file),csvDir,type)
            print(file)
def writeOut(data,path,type):
    if type == "P":
        writing = open(path+"\Player.csv", "a",encoding = 'utf-8-sig')
    elif type == "C":
        writing = open(path+"\Country.csv", "a",encoding = 'utf-8-sig')
    elif type == "PO":
        writing = open(path+"\Position.csv", "a",encoding = 'utf-8-sig')
    for i in data:
        writing.write(i+"\n")
    writing.close()
def makeUnique(filename):
    found = {"-1"}
    data = []
    reading = open(filename,"r", encoding='utf-8-sig')
    currLine = reading.readline()
    while True:
        if currLine == "":
            break
        else:
            id = currLine.split(",")[0]
            id = id.split("(")[1]
            id = id.strip()
            if id not in found:
                data.append(currLine)
                found.add(id)
        currLine = reading.readline()
    reading.close()
    writing = open("New" + filename, "a",encoding = 'utf-8-sig')
    for i in data:
        writing.write(i)
    os.remove(filename)
csvDir = os.getcwd()
callConvert(".",csvDir,"PO")
#callConvert(".",csvDir,"P")
#makeUnique("Player.csv")
#callConvert(".",csvDir,"C")
#makeUnique("Country.csv")