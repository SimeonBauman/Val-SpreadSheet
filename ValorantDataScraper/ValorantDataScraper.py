file_path = r'ValStats.txt'
SpecialCharacter = r'SpecialCharacter.txt'

class Map:
    def __init__(self,name):
        self.name = name
        self.wins = 0
        self.losses = 0
        self.DefWin = 0
        self.DefLoss = 0
        self.AtkWin = 0
        self.AtkLoss = 0
    
    def countRounds(self, side, num):
        if num == -1:
            if side == "Def": self.DefLoss += 1
            else: self.AtkLoss +=1
        else:
            if side == "Def": self.DefWin += 1
            else: self.AtkWin +=1
    


def getSpecialCharacter():
    with open(SpecialCharacter) as file:
        line_list = file.readlines()
        line_list = [item.rstrip() for item in line_list]
        return line_list

def getData():
    with open(file_path) as file:
        line_list = file.readlines()
        line_list = [item.rstrip() for item in line_list]
        return line_list

def getTeam(data, player):
    i = data.index(player) - 1
    while (i > 0):
        if data[i] == "Team A":
            return "Atk"
        elif data[i] == "Team B":
            return "Def"
        i = i - 1

def getMap(map,maps):
    i = 0
    while i < len(maps) - 1:
        if maps[i].name == map: return i
        i += 1
        
def getTotalRounds(data,maps,team, mapIndex):
    t1 = int(data[data.index("Team A") + 1])
    t2 = int(data[data.index("Team B") + 1])
    if (team == "Def" and t2 > t1) or (team == "Atk" and t1 > t2):
        maps[mapIndex].wins += 1
    else:
        maps[mapIndex].losses += 1
    return  t1 + t2

def getSplitRounds(data, map, totalRounds, team,sp):
    i = 1
    index = data.index(sp[0])
    side = 0
    if team == "Def": side = 1
    else: side = 2
    while data[index] != "1":
        index += 1
        
    while i <= totalRounds:
        if i == 13:
            if side == 1: team = "Atk"
            else: team = "Def"
        if data[index - side] == sp[0]:
            map.countRounds(team,-1)
        else:
            map.countRounds(team,1)
            
        index += 3
        i += 1

def printResults(map,Maps):
    print(Maps[map].name)
    print(Maps[map].wins)
    print(Maps[map].losses)
    print(Maps[map].DefWin)
    print(Maps[map].DefLoss)
    print(Maps[map].AtkWin)
    print(Maps[map].AtkLoss)


def main():
    sp = getSpecialCharacter()
    maps = [Map("Abyss"), Map("Ascent")]
    team = ""
    mapIndex = -1
    totalRounds = 0
    data = getData()
    team = getTeam(data, "CUW Lock")
    mapIndex = getMap(data[2],maps)
    totalRounds = getTotalRounds(data,maps,team,mapIndex)
    getSplitRounds(data,maps[mapIndex],totalRounds, team,sp)
    printResults(mapIndex,maps)
    
    
if __name__=="__main__": 
    main() 
    


    



    
