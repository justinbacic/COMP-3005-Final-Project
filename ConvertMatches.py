#Matches JSON files hold the info needed for the Matches relation, Referee, Teams, Country, Managers, Competition_Stage, and Stadium  relation
import os, sys
def convertMatches(filename):
    reading = open(filename,"r", encoding='utf-8')
    currLine = reading.readline()
    matches = []
    while currLine != "":
        while "match_id" not in currLine and currLine != "":
            currLine = reading.readline() 
        match_id = "null"
        match_date = "null"
        kick_off = "null"
        home_score ="null"
        away_score = "null"
        match_week = "null"
        season_id = "null"
        stage_name = "null" 
        stadium_id = "null"
        home_team_id = "null"
        home_team_manager_id = "null" 
        away_team_id = "null" 
        away_team_manager_id = "null" 
        referee_id = "null"
        if currLine !="":
           match_id = extractVal(currLine)
        else:
            break
        currMatch = ""
        currLine = reading.readline()
        while "match_id" not in currLine:
            val = extractVal(currLine)
            if "match_date" in currLine:
                match_date = val
                currLine = reading.readline()
                continue
            if "kick_off" in currLine:
                kick_off = val
                currLine = reading.readline()
                continue
            if "home_score" in currLine:
                home_score = val
                currLine = reading.readline()
                continue
            if "away_score" in currLine:
                away_score = val
                currLine = reading.readline()
                continue
            if "match_week" in currLine:
                match_week = val
                currLine = reading.readline()
                continue
            if "season_id" in currLine:
                season_id = val
                currLine = reading.readline()
                continue
            if "competition_stage" in currLine:
                while "name" not in currLine:
                    currLine = reading.readline()
                    if currLine =="":
                        break
                val = extractVal(currLine)
                stage_name = val
                currLine = reading.readline()
                continue
            if "stadium" in currLine:
                while "id" not in currLine:
                    currLine = reading.readline()
                    if currLine =="":
                        break
                val = extractVal(currLine)
                stadium_id = val
                currLine = reading.readline()
                continue
            if "home_team_id" in currLine:
                home_team_id = val
                while "managers" not in currLine:
                    currLine = reading.readline()
                    if currLine =="":
                        break
                while "id" not in currLine:
                    currLine = reading.readline()
                    if currLine =="":
                        break
                val = extractVal(currLine)
                home_team_manager_id = val
                currLine = reading.readline()
                continue
            if "away_team_id" in currLine:
                away_team_id = val
                while "managers" not in currLine:
                    currLine = reading.readline()
                    if currLine =="":
                        break
                while "id" not in currLine:
                    currLine = reading.readline()
                    if currLine =="":
                        break
                val = extractVal(currLine)
                away_team_manager_id = val
                currLine = reading.readline()
                continue
            if "referee" in currLine:
                while "id" not in currLine:
                    currLine = reading.readline()
                    if currLine =="":
                        break
                val = extractVal(currLine)
                referee_id = val
                currLine = reading.readline()
                continue
            currLine = reading.readline()
            if(currLine == ""):
                break
        currMatch = "("+match_id+", "+match_date+", "+kick_off+", "+home_score+", "+away_score+", "+match_week+", "+season_id+", "+ stage_name+", "+stadium_id+", "+home_team_id+", "+home_team_manager_id+", "+away_team_id+", "+away_team_manager_id+", "+referee_id+")"
        currMatch = currMatch.replace('"',"'")
        matches.append(currMatch)
    reading.close()
    return matches
def extractVal(str):
    arr = str.split(':',1)
    ret = ""
    if len(arr) > 1:
        ret = arr[1].split(',')[0].strip()
    return ret
def convertTeams(filename):
    reading = open(filename,"r", encoding='utf-8')
    currLine = reading.readline()
    teamsFound = {"-1"}
    teamData = []
    while currLine != "":
        while "home_team_id" not in currLine and currLine != "":
            currLine = reading.readline() 
        team_id = "null"
        team_name = "null"
        country_id = "null"
        if currLine =="":
           
           break
        else:
            team_id = extractVal(currLine)
        currTeam = ""
        currLine = reading.readline()
        while "away_team_id" not in currLine:
            val = extractVal(currLine)
            if "home_team_name" in currLine:
                team_name = val
                currLine = reading.readline()
                continue
            if "country" in currLine:
                while "id" not in currLine:
                    currLine = reading.readline()
                    if currLine =="":
                        break
                val = extractVal(currLine)
                country_id = val
                currLine = reading.readline()
                continue
            currLine = reading.readline()
            if(currLine == ""):
                break
        if team_id not in teamsFound:
            currTeam = "("+team_id+", "+team_name+", "+country_id+"),"
            currTeam = currTeam.replace('"',"'")
            teamData.append(currTeam)
            teamsFound.add(team_id)
        team_id = "null"
        team_name = "null"
        country_id = "null"
        team_id = extractVal(currLine)
        while "home_team" not in currLine:
            val = extractVal(currLine)
            if "away_team_name" in currLine:
                team_name = val
                currLine = reading.readline()
                continue
            if "country" in currLine:
                while "id" not in currLine:
                    currLine = reading.readline()
                    if currLine =="":
                        break
                val = extractVal(currLine)
                country_id = val
                currLine = reading.readline()
                continue
            currLine = reading.readline()
            if(currLine == ""):
                break
        if team_id not in teamsFound:
            currTeam = "("+team_id+", "+team_name+", "+country_id+")"
            currTeam = currTeam.replace('"',"'")
            teamData.append(currTeam)
            teamsFound.add(team_id)
    reading.close()
    return teamData
def convertRefs(filename):
    reading = open(filename,"r", encoding = 'utf-8')
    refereesFound = {"-1"}
    refereeData = []
    currLine = reading.readline()
    while currLine != "":
        while "referee" not in currLine and currLine != "":
            currLine = reading.readline() 
        referee_id = "null"
        referee_name = "null"
        country_id = "null"
        if currLine =="":
           break
        currRef = ""
        currLine = reading.readline()
        referee_id = extractVal(currLine)
        currLine = reading.readline()
        referee_name = extractVal(currLine)
        currLine = reading.readline()
        currLine = reading.readline()
        country_id = extractVal(currLine)
        if referee_id not in refereesFound:
            currRef = "("+referee_id+", "+referee_name+", "+country_id+")"
            currRef = currRef.replace('"',"'")
            refereeData.append(currRef)
            refereesFound.add(referee_id)
        currLine = reading.readline()
    reading.close()
    return refereeData
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
def convertManagers(filename):
    reading = open(filename,"r", encoding = 'utf-8')
    managersFound = {"-1"}
    managerData = []
    currLine = reading.readline()
    while currLine != "":
        while "managers" not in currLine and currLine != "":
            currLine = reading.readline() 
        manager_id = "null"
        manager_name = "null"
        nickname = "null"
        date_of_birth = "null"
        country_id = "null"
        if currLine =="":
           break
        currMan = ""
        currLine = reading.readline()
        manager_id = extractVal(currLine)
        currLine = reading.readline()
        manager_name = extractVal(currLine)
        currLine = reading.readline()
        nickname = extractVal(currLine)
        currLine = reading.readline()
        date_of_birth = extractVal(currLine)
        currLine = reading.readline()
        currLine = reading.readline()
        country_id = extractVal(currLine)
        currLine = reading.readline()
        if manager_id not in managersFound:
            currMan = "("+manager_id+", "+manager_name+", "+nickname+", "+date_of_birth+", "+country_id+")"
            currMan = currMan.replace('"',"'")
            managerData.append(currMan)
            managersFound.add(manager_id)
        currLine = reading.readline()
    reading.close()
    return managerData
def convertStages(filename):
    reading = open(filename,"r", encoding = 'utf-8')
    stagesFound = {"-1"}
    stageData = []
    currLine = reading.readline()
    while currLine != "":
        while "competition_stage" not in currLine and currLine != "":
            currLine = reading.readline() 
        stage_id = "null"
        stage_name = "null"
        if currLine =="":
           break
        currStage = ""
        currLine = reading.readline()
        stage_id = extractVal(currLine)
        currLine = reading.readline()
        stage_name = extractVal(currLine)
        if stage_id not in stagesFound:
            currStage = "("+stage_id+", "+stage_name+")"
            currStage = currStage.replace('"',"'")
            stageData.append(currStage)
            stagesFound.add(stage_id)
        currLine = reading.readline()
    reading.close()
    return stageData
def convertStadiums(filename):
    reading = open(filename,"r", encoding = 'utf-8')
    stadiumsFound = {"-1"}
    stadiumData = []
    currLine = reading.readline()
    while currLine != "":
        while "stadium" not in currLine and currLine != "":
            currLine = reading.readline() 
        stadium_id = "null"
        stadium_name = "null"
        country_id = "null"
        if currLine =="":
           break
        currStadium = ""
        currLine = reading.readline()
        stadium_id = extractVal(currLine)
        currLine = reading.readline()
        stadium_name = extractVal(currLine)
        currLine = reading.readline()
        currLine = reading.readline()
        country_id = extractVal(currLine)
        if stadium_id not in stadiumsFound:
            currStadium = "("+stadium_id+", "+stadium_name+", "+country_id+")"
            currStadium = currStadium.replace('"',"'")
            stadiumData.append(currStadium)
            stadiumsFound.add(stadium_id)
        currLine = reading.readline()
    reading.close()
    return stadiumData
def writeOut(data,path,type):
    if type == "M":
        writing = open(path+"\Match.csv", "a",encoding = 'utf-8-sig')
    elif type == "T":
        writing = open(path+"\Team.csv", "a",encoding = 'utf-8-sig')
    elif type == "R":
        writing = open(path+"\Referee.csv", "a",encoding = 'utf-8-sig')
    elif type == "C":
        writing = open(path+"\Country.csv", "a",encoding = 'utf-8-sig')
    elif type == "MAN":
        writing = open(path+"\Manager.csv", "a",encoding = 'utf-8-sig')
    elif type == "ST":
        writing = open(path+"\Stage.csv", "a",encoding = 'utf-8-sig')
    elif type == "STAD":
        writing = open(path+"\Stadium.csv", "a",encoding = 'utf-8-sig')
    for i in data:
        writing.write(i+"\n")
    writing.close()
def callConvert(path,csvDir,type):
    dir = os.listdir(path)
    foundSet = {"-1"}
    for file in dir:
        if os.path.isdir(file):
            curDir = os.getcwd()
            os.chdir("./"+file)
            callConvert(".",csvDir,type)
            os.chdir(curDir)
        elif "a"not in file and"e"not in file and "u"not in file:
            if type == "M":
                writeOut(convertMatches(file),csvDir,type)
            if type == "T":
                writeOut(convertTeams(file),csvDir,type)
            if type == "R":
                writeOut(convertRefs(file),csvDir,type)
            if type == "C":
                writeOut(convertCountries(file),csvDir,type)
            if type == "MAN":
                writeOut(convertManagers(file),csvDir,type)
            if type == "ST":
                writeOut(convertStages(file),csvDir,type)
            if type == "STAD":
                writeOut(convertStadiums(file),csvDir,type)
            print(file)
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
callConvert(".",csvDir,"M")
callConvert(".",csvDir,"R")
makeUnique("Referee.csv")
callConvert(".",csvDir,"T")
makeUnique("Team.csv")
'''callConvert(".",csvDir,"C")
makeUnique("Country.csv")'''
callConvert(".",csvDir,"MAN")
makeUnique("Manager.csv")
callConvert(".",csvDir,"ST")
makeUnique("Stage.csv")
callConvert(".",csvDir,"STAD")
makeUnique("Stadium.csv")
