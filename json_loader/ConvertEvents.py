#Information in the events files have data for Event, Block, Ball_Reciept, Dribble, Dribbled_Past, Pass, Shot, Carry, Foul_Committed, Foul_Won, Goal_Keeper, Interception
import os
def convertEvents(filename):
    reading = open(filename,"r", encoding='utf-8')
    currLine = reading.readline()
    eventsData = []
    match_id = filename.split(".")[0]
    while currLine != "":
        while currLine != "}, {\n" and currLine != "":
            currLine = reading.readline() 
        event_id = "null"
        index = "null"
        period = "null"
        timestamp ="null"
        type_id ="null"
        type_name = "null"
        possession = "null"
        posession_team_id = "null"
        play_pattern_name = "null"
        event_team_id = "null"
        player_id = "null"
        position = "null"
        location_x = "null"
        location_y = "null"
        duration = "null"
        under_pressure = "null"
        out ="null"
        if currLine =="":
           break
        currLine = reading.readline()
        event_id = extractVal(currLine)
        currLine = reading.readline()
        currEvent = ""
        while currLine != "}, {\n" and currLine != "":
            if "index" in currLine and index == "null":
                index = extractVal(currLine)
                currLine = reading.readline()
                continue
            elif "period" in currLine and period == "null":
                period = extractVal(currLine)
                currLine = reading.readline()
                continue
            elif "timestamp" in currLine and timestamp == "null":
                timestamp = extractVal(currLine)
                currLine = reading.readline()
                continue
            elif "type" in currLine and type_id =="null":
                currLine = reading.readline()
                type_id = extractVal(currLine)
                currLine = reading.readline()
                type_name = extractVal(currLine)
                currLine = reading.readline()
                continue
            elif "possession" in currLine:
                possession = extractVal(currLine)
                currLine = reading.readline()
                currLine = reading.readline()
                posession_team_id = extractVal(currLine)
                currLine = reading.readline()
                continue
            elif "play_pattern" in currLine:
                currLine = reading.readline()
                currLine = reading.readline()
                play_pattern_name = extractVal(currLine)
                currLine = reading.readline()
                continue
            elif '"team"' in currLine and event_team_id == "null":
                currLine = reading.readline()
                event_team_id = extractVal(currLine)
                currLine = reading.readline()
                continue
            elif "player" in currLine and player_id == "null":
                currLine = reading.readline()
                player_id = extractVal(currLine)
                currLine = reading.readline()
                continue
            elif "position" in currLine and position == "null":
                currLine = reading.readline()
                currLine = reading.readline()
                position = extractVal(currLine)
                currLine = reading.readline()
                continue
            elif '"location"' in currLine and location_x == "null":
                location_x = extractLocation(currLine,1)
                location_y = extractLocation(currLine,2)
                currLine = reading.readline()
                continue
            elif "duration" in currLine:
                duration = extractVal(currLine)
                currLine = reading.readline()
                continue
            elif "under_pressure" in currLine:
                under_pressure = extractVal(currLine)
                currLine = reading.readline()
                continue
            elif '"out"' in currLine:
                out = extractVal(currLine)
                currLine = reading.readline()
                continue
            else:
                currLine = reading.readline()
        if type_id == "35" or type_id == "36":
            continue
        currEvent = "("+event_id +", " + match_id +", "+index +", "+period +", "+  timestamp +", "+type_id +", "+type_name +", "+possession +", "+posession_team_id +", "+play_pattern_name +", "+event_team_id +", "+player_id +", "+position +", "+location_x +", "+location_y +", "+        duration +", "+        under_pressure +", "+out+"),"
        currEvent = currEvent.replace('"',"'")
        eventsData.append(currEvent)
    reading.close()
    return eventsData
def convertSubevents(filename):
    reading = open(filename,"r", encoding='utf-8')
    currLine = reading.readline()
    eventsData = []
    match_id = filename.split(".")[0]
    while currLine != "":
        while currLine != "}, {\n" and currLine != "":
            currLine = reading.readline() 
        event_id = "null"
        type_id ="null"
        if currLine =="":
           break
        currEvent = []
        currLine = reading.readline()
        event_id = extractVal(currLine)
        currLine = reading.readline()
        currEvent.append(currLine)
        while currLine != "}, {\n" and currLine != "":
            if "type"  in currLine and type_id =="null":
                currLine = reading.readline()
                currEvent.append(currLine)
                type_id = extractVal(currLine)
                currLine = reading.readline()
                currEvent.append(currLine)
                continue
            else:
                currLine = reading.readline()
                currEvent.append(currLine)
        if type_id == "35" or type_id == "36":
            continue
        else:
            proccessEvent(currEvent,type_id,event_id)
    reading.close()
def proccessEvent(eventData, eventType, event_id):
    data = ""
    if  eventType == "6": #block
        counterpress = "null"
        deflection = "null"
        offensive = "null"
        save_block = "null"
        for i in eventData:
            if "counterpress" in i:
                counterpress = extractVal(i)
            if "deflection" in i:
                deflection = extractVal(i)
            if "offensive" in i:
                offensive = extractVal(i)
            if "save_block" in i:
                save_block = extractVal(i)
        data = "(" + event_id +", "+counterpress+", "+deflection+", "+offensive+", "+save_block+")"
    elif eventType == "42": #ball reciept
        outcome = "null"
        for i in range(0,len(eventData)):
            if "outcome" in eventData[i]:
                outcome = extractVal(eventData[i+2])
        data = "(" + event_id +", "+outcome+")"
    elif eventType == "14": #dribble
        outcome = "null"
        nutmeg = "null"
        overrun = "null"
        no_touch = "null"
        for i in range(0,len(eventData)):
            if "outcome" in eventData[i]:
                outcome = extractVal(eventData[i+2])
            if "nutmeg" in eventData[i]:
                nutmeg = extractVal(eventData[i])
            if "overrun" in eventData[i]:
                overrun = extractVal(eventData[i])
            if "no_touch" in eventData[i]:
                no_touch = extractVal(eventData[i])
        data = "(" + event_id +", "+outcome+", "+nutmeg+", "+overrun+", "+no_touch+")"
    elif eventType == "39": #dribble past
        counterpress = "null"
        for i in eventData:
            if "counterpress" in i:
                counterpress = extractVal(i)
        data = "(" + event_id +", "+counterpress+")"
    elif eventType == "30": #pass
        recipiant_player_id = "null"
        length ="null"
        angle = "null"
        height = "null"
        end_location_x = "null"
        end_location_y = "null"
        body_part = "null"
        type = "null"
        outcome = "null"
        technique = "null"
        deflected = "null"
        miscommunication = "null"
        for i in range(0,len(eventData)):
            if "outcome" in eventData[i]:
                outcome = extractVal(eventData[i+2])
            if "recipient" in eventData[i]:
                recipiant_player_id = extractVal(eventData[i+1])
            if "height" in eventData[i]:
                height = extractVal(eventData[i+2])
            if "body_part" in eventData[i]:
                body_part = extractVal(eventData[i+2])
            if "length" in eventData[i]:
                length = extractVal(eventData[i])
            if "angle" in eventData[i]:
                angle = extractVal(eventData[i])
            if "end_location" in eventData[i]:
                end_location_x = extractLocation(eventData[i],1)
                end_location_y = extractLocation(eventData[i],2)
            if "type" in eventData[i]:
                type = extractVal(eventData[i+2])
            if "technique" in eventData[i]:
                technique = extractVal(eventData[i+2])
            if "deflected" in eventData[i]:
                deflected = extractVal(eventData[i])
            if "miscommunication" in eventData[i]:
                miscommunication = extractVal(eventData[i])
        data = "("+event_id+", "+recipiant_player_id+", "+length+", "+angle+", "+height+", "+end_location_x+", "+end_location_y+", "+body_part+", "+type+", "+outcome+", "+technique+", "+deflected+", "+miscommunication+")"
    elif eventType == "16": #shot
        end_location_x = "null"
        end_location_y = "null"
        end_location_z ="null"
        first_time ="null"
        xg_score = "null"
        deflected = "null"
        technique = "null"
        body_part = "null"
        type = "null"
        outcome = "null"
        for i in range(0,len(eventData)):
            if "outcome" in eventData[i]:
                outcome = extractVal(eventData[i+2])
            if "technique" in eventData[i]:
                technique = extractVal(eventData[i+2])
            if "body_part" in eventData[i]:
                body_part = extractVal(eventData[i+2])
            if "end_location" in eventData[i]:
                end_location_x = extractLocation(eventData[i],1)
                end_location_y = extractLocation(eventData[i],2)
                end_location_z = extractLocation(eventData[i],3)
            if "first_time" in eventData[i]:
                first_time = extractVal(eventData[i])
            if "xg" in eventData[i]:
                xg_score = extractVal(eventData[i])
            if "type" in eventData[i]:
                type = extractVal(eventData[i+2])
            if "deflected" in eventData[i]:
                deflected = extractVal(eventData[i])
        data = "("+event_id+", "+ end_location_x+", "+end_location_y+", "+end_location_z+", "+first_time+", "+xg_score+", "+deflected+", "+technique+", "+body_part+", "+type+", "+outcome+")"
    elif eventType == "43": #carry
        end_location_x = "null"
        end_location_y = "null"
        for i in eventData:
            if "end_location" in i:
                end_location_x = extractLocation(i,1)
                end_location_y = extractLocation(i,2)
        data = "(" + event_id +", "+end_location_x+", "+end_location_y+")"
    elif eventType == "22": #foul committed
        advantage = "null"
        counterpress = "null"
        offensive = "null"
        penalty = "null"
        card = "null"
        type = "null"
        for i in range(0,len(eventData)):
            if "card" in eventData[i]:
                card = extractVal(eventData[i+2])
                i +=2
            if "type" in eventData[i]:
                type = extractVal(eventData[i+2])
            if "advantage" in eventData[i]:
                advantage = extractVal(eventData[i])
            if "counterpress" in eventData[i]:
                counterpress = extractVal(eventData[i])
            if "offensive" in eventData[i]:
                offensive = extractVal(eventData[i])
            if "penalty" in eventData[i]:
                penalty = extractVal(eventData[i])
        data = "("+event_id+", "+advantage+", "+counterpress+", "+offensive+", "+penalty+", "+card+", "+type+")"
    elif eventType == "21": #foul won
        advantage = "null"
        defensive = "null"
        penalty = "null"
        for i in eventData:
            if "advantage" in i:
                advantage = extractVal(i)
            if "defensive" in i:
                defensive = extractVal(i)
            if "penalty" in i:
                penalty = extractVal(i)
        data = "("+event_id+", "+advantage+", "+defensive+", "+penalty+")"
    elif eventType == "23": #goal keeper
        position = "null"
        technique = "null"
        body_part = "null"
        type = "null"
        outcome = "null"
        for i in range(0,len(eventData)):
            if "outcome" in eventData[i]:
                outcome = extractVal(eventData[i+2])
            if "position" in eventData[i]:
                position = extractVal(eventData[i+2])
            if "technique" in eventData[i]:
                technique = extractVal(eventData[i+2])
            if "body_part" in eventData[i]:
                body_part = extractVal(eventData[i+2])
            if "type" in eventData[i]:
                type = extractVal(eventData[i+2])
        data = "("+event_id+", "+position+", "+technique+", "+body_part+", "+type+", "+outcome+")"
    elif eventType == "10": #interception
        outcome = "null"
        for i in range(0,len(eventData)):
            if "outcome" in eventData[i]:
                outcome = extractVal(eventData[i+2])
        data = "(" + event_id +", "+outcome+")"
    elif eventType == "4": #duel
        outcome = "null"
        counterpress = "null"
        for i in range(0,len(eventData)):
            if "outcome" in eventData[i]:
                outcome = extractVal(eventData[i+2])
            if "counterpress" in eventData[i]:
                counterpress = extractVal(eventData[i])
        data = "(" + event_id +", "+counterpress+", "+outcome+")"
    else:
        return
        #Do nothing
    data = data.replace('"',"'")
    data = data +","
    writeSubevent(data,eventType)
def writeSubevent(eventData, type):
    if type == "6":
        #block
        writing = open("Block.csv", "a",encoding = 'utf-8-sig')
    elif type == "42":
        #ball reciept
        writing = open("Ball_Reciept.csv", "a",encoding = 'utf-8-sig')
    elif type == "14":
        #dribble 
        writing = open("Dribble.csv", "a",encoding = 'utf-8-sig')
    elif type == "39":
        #dribble past
        writing = open("Dribble_Past.csv", "a",encoding = 'utf-8-sig')
    elif type == "30":
        #pass
        writing = open("Pass.csv", "a",encoding = 'utf-8-sig')
    elif type == "16":
        #shot
        writing = open("Shot.csv", "a",encoding = 'utf-8-sig')
    elif type == "43":
        #carry
        writing = open("Carry.csv", "a",encoding = 'utf-8-sig')
    elif type == "22":
        #foul committed
        writing = open("Foul_Committed.csv", "a",encoding = 'utf-8-sig')
    elif type == "21":
        #foul won
        writing = open("Foul_Won.csv", "a",encoding = 'utf-8-sig')
    elif type == "23":
        #goal keeper
        writing = open("Goal_Keeper.csv", "a",encoding = 'utf-8-sig')
    elif type == "10":
        #interception
        writing = open("Interception.csv", "a",encoding = 'utf-8-sig')
    elif type == "4":
        #duel
        writing = open("Duel.csv", "a",encoding = 'utf-8-sig')
    writing.write(eventData+"\n")
    writing.close()
def extractVal(str):
    arr = str.split(':',1)
    ret = ""
    if len(arr) > 1:
        ret = arr[1].split(',')[0].strip()
    return ret
def extractLocation(str,num):
    arr = str.split(':',1)
    ret = "null"
    if len(arr) > 1:
        ret = arr[1].split("[")[1]
        ret = ret.split("]")[0]
        ret = ret.split(",")
        if num == 1:
            return ret[0].strip()
        elif num == 2:
            return ret[1].strip()
        elif num == 3 and len(ret) > 2:
            return ret[2].strip()
    return "null"
def callConvert(path,csvDir,type):
    dir = os.listdir(path)
    for file in dir:
        if os.path.isdir(file):
            curDir = os.getcwd()
            os.chdir("./"+file)
            callConvert(".",csvDir,type)
            os.chdir(curDir)
        elif "a"not in file and"e"not in file and "u"not in file and "i"not in file and "h"not in file and "l"not in file:
            if type == "E":
                writeOut(convertEvents(file),csvDir,type)
            if type == "S":
                convertSubevents(file)
            print(file)
def countShots(filename, count):
    reading = open(filename,"r", encoding='utf-8')
    currLine = reading.readline()
    while currLine != "":
        if '"shot" :' in currLine:
            count += 1
        currLine = reading.readline()
    reading.close()
    return count
def callCount(path):
    dir = os.listdir(path)
    count = 0
    for file in dir:
        if "vert" not in file:
            count = countShots(file,count)
    return count
def writeOut(data,path,type):
    if type == "E":
        writing = open(path+"\Event.csv", "a",encoding = 'utf-8-sig')
    for i in data:
        writing.write(i+"\n")
    writing.close()
csvDir = os.getcwd()
callConvert(".",csvDir,"E")
#callConvert(".",csvDir,"S")

