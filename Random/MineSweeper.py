import sys
import os
import random

####################
print("Enter Grid Size:",end=' ')
gs=input().split()
gridSize=(int(gs[0]),int(gs[1]))

print("Enter Number of Mines:",end=' ')

noOfMines=int(input())
#####################


totalCells=gridSize[0]*gridSize[1]

table=['?' for _ in range(totalCells)]

tableAns=[0 for _ in range(totalCells)]

def Error(x):
    print(x)
    sys.exit()

if(noOfMines>totalCells):
    Error("Number of Mines too large")

cellsLeft=totalCells-noOfMines

def ChangeCell(x,y,Z):
    global table,gridSize
    if(x>=gridSize[0] or y>=gridSize[1]):
        Error("ChangeCell")
    table[x*gridSize[1]+y]=Z

def GetCell(x,y,F=False):
    global table,gridSize
    if(x>=gridSize[0] or y>=gridSize[1]):
        Error("GetCell")
    if(not(F)):
        return table[x*gridSize[1]+y]
    return tableAns[x*gridSize[1]+y]

def PrintTable(x=False):
    global table,gridSize,tableAns
    print("  ",end=' ')
    for i in range(0,gridSize[1]):
        print(i,end=' ')
    print("")
    for i in range(0,gridSize[1]+1):
        print('--',end='')
    print("")

    for i in range(0,gridSize[0]):
        print(str(i)+'|',end=' ')
        for j in range(0,gridSize[1]):
            if(x):
                print(tableAns[i*gridSize[1]+j],end=" ")
                continue
            print(table[i*gridSize[1]+j],end=" ")
        print("")

def CheckAndAdd(x,y):
    if(x>=gridSize[0] or y>=gridSize[1] or x<0 or y<0 or GetCell(x,y,True)=='X'):
        return
    tableAns[x*gridSize[1]+y]+=1

def Change_Ans(t):
    x=t//gridSize[0]
    y=t%gridSize[1]
    tableAns[t]='X'
    temp=[(x+1,y),(x,y+1),(x-1,y),(x,y-1),(x+1,y+1),(x-1,y+1),(x-1,y-1),(x+1,y-1)]
    for t in temp:
        CheckAndAdd(t[0],t[1])
    

dict_exist={}

for _ in range(0,noOfMines):
    t=random.randint(0,totalCells-1)
    while t in dict_exist:
        t+=1
    dict_exist[t]=1
    # table[t]='X'
    Change_Ans(t)


def Moved(x,y):
    temp=[(x+1,y),(x,y+1),(x-1,y),(x,y-1),(x+1,y+1),(x-1,y+1),(x-1,y-1),(x+1,y-1)]
    for t in temp:
        if(t[0]>=0 and t[0]<gridSize[0] and t[1]>=0 and t[1]<gridSize[1]):
            if(GetCell(t[0],t[1],True)!='X'):
                Move(t[0],t[1])

def Move(m,n):
    global cellsLeft
    cell=GetCell(m,n,True)
    if(cell=='X'):
        print("Game Over!!!")
        input()
        sys.exit()

    if(GetCell(m,n)=='?'):
        if(cell==0):
            ChangeCell(m,n,0)    
            Moved(m,n)
        else:
            ChangeCell(m,n,cell)
        cellsLeft-=1

def firstMove(m,n):
    global cellsLeft
    cell=GetCell(m,n,True)
    if(cell=='X'):
        print("Game Over")
        input()
        sys.exit()

    if(GetCell(m,n)=='?'):
        if(cell==0 or cell==1):
            ChangeCell(m,n,cell)
            Moved(m,n)
        else:
            ChangeCell(m,n,cell)
        cellsLeft-=1
def isInside(x,y):
    if(x>=0 and x<gridSize[0] and y>=0 and y<gridSize[1]):
        return True
    return False    
#########################

first=False
while cellsLeft>0:
    PrintTable()
    print("")
    # PrintTable(True)
    print("--------")
    i=input().split()
    if(i[0]=='F' or i[0]=='f'):
        if(GetCell(int(i[1]),int(i[2]))=='F'):
            ChangeCell(int(i[1]),int(i[2]),'?')
        else:
            ChangeCell(int(i[1]),int(i[2]),'F')
    elif(not(first)):
        Move(int(i[0]),int(i[1]))
    elif(first):
        firstMove(int(i[0]),int(i[1]))
        first=False
    os.system("cls")
    
print("-----")
PrintTable()
print("YOU WON!!!")
input()
sys.exit()