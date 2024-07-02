import xlwt
from xlwt import Workbook 

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

def getData(file_path):
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

def getMap(data,maps):
    i = data.index("Normal")
    while data[i] == "Normal":
        i+=1
    j = 0
    while j < len(maps):
        if maps[j].name == data[i]: return j
        j += 1
        
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

def ClearMap(data):
    while data[0] !="/?/":
        data.pop(0)
    data.pop(0)

def printResults(Maps):
    for map in Maps:
        print(map.name)
        print(map.wins)
        print(map.losses)
        print(map.DefWin)
        print(map.DefLoss)
        print(map.AtkWin)
        print(map.AtkLoss)

def createSpeadSheet(Maps,path): 
    wb = Workbook() 
    sheet1 = wb.add_sheet('Sheet 1') 
    i = 0 
    for map in Maps:
        sheet1.write(0,i,map.name)
        sheet1.write(1,i,map.wins)
        sheet1.write(2,i,map.losses)
        sheet1.write(3,i,str(map.DefWin) + "-" + str(map.DefLoss))
        sheet1.write(4,i,str(map.AtkWin) + "-" + str(map.AtkLoss))
        sheet1.write(5,i,str(map.AtkWin + map.DefWin) + "-" + str(map.AtkLoss + map.DefLoss))
        i += 1
    wb.save("finalized.xls")
       


def main():
    sp = getSpecialCharacter()
    maps = [Map("Abyss"), Map("Ascent"), Map("Breeze"), Map("Bind"), Map("Fracture"), Map("Haven"), Map("Icebox"), Map("Lotus"), Map("Pearl"), Map("Split"), Map("Sunset")]
    team = ""
    mapIndex = -1
    totalRounds = 0
    IGN = input("Enter IGN\n")
    file_path = "Stats\\" + input("Enter File Name\n") + ".txt"
    data = getData(file_path)
    while len(data) > 0:
        team = getTeam(data, IGN)
        mapIndex = getMap(data,maps)
        totalRounds = getTotalRounds(data,maps,team,mapIndex)
        getSplitRounds(data,maps[mapIndex],totalRounds, team,sp)
        ClearMap(data)
    printResults(maps)
    createSpeadSheet(maps, file_path)
    
    
if __name__=="__main__": 
    main() 
    
