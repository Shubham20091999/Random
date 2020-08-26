import math
funs={'sin':math.sin,'cos':math.cos,'tan':math.tan,'asin':math.asin,'acos':math.acos,'atan':math.atan,'sinh':math.sinh,'cosh':math.cosh,'tanh':math.tanh,'ln':math.log,'log':math.log10}
# 'asin','acos','atan','acsc','asec','acot','hsin','hcos','htan','hcsc','hsec','hcot','ln','log'
def getNum(a):#Get Number if input is Number str
    try:
        return float(a)
    except:
        t=a.split('.')
        return float(t[0])+float(t[1])/pow(10,len(t[1]))

def AllOperator(input):#Operate On Without Brackets
    Funcs(input)
    operate(input,['^'])
    operate(input,['*','/'])
    if(input[0]=='-'):
        input.pop(0)
        input[0]*=-1
    operate(input,['+','-'])
    return input

def Brac(a):#Resolve Brackets
    inPos=[]#incomplete Pos Of Brackets (LL is Known)
    Pos=[]#Complete Pos of Brackets ( UL and LL is Known)
    for i in range(len(a)):#Getting Bracket Position
        if(a[i]=='('):
            inPos.append([i,-1])
        elif(a[i]==')'):
            inPos[-1][1]=i
            Pos.append(inPos.pop(-1))
    if(len(Pos)==0):
        return
    newPos=[tuple(Pos[0])]#For final position of each brackets after computation inside that bracket and all the computation before that bracket
    for i in range(1,len(Pos)):
        LL=0
        RR=0
        for j in range(0,i):
            D=newPos[j][1]-newPos[j][0]
            if(Pos[i][0]>Pos[j][1]):
                LL+=D
            RR+=D
        newPos.append((Pos[i][0]-LL,Pos[i][1]-RR))
    Pos=newPos

    for p in Pos:#Computing and Replacing Brackets to values
        val=AllOperator(a[p[0]+1:p[1]])[0]
        del a[p[0]:p[1]+1]
        a.insert(p[0],val)
    return a

def operate(a,op):#operate a specific operator
    i=0
    while i<len(a):
        if(a[i] in op):
            m=1
            temp=a[i]
            if(a[i+1]=='-'):
                m=-1
                a.pop(i)
            if(type(a[i+1])==float and type(a[i-1])==float):
                if(temp=='^'):
                    a[i-1]=pow(a[i-1],m*a[i+1])
                elif(temp=='/'):
                    a[i-1]=a[i-1]/(m*a[i+1])
                elif(temp=='*'):
                    a[i-1]=a[i-1]*m*a[i+1]
                elif(temp=='+'):
                    a[i-1]=a[i-1]+a[i+1]
                elif(temp=='-'):
                    a[i-1]=a[i-1]-a[i+1]
            del a[i:i+2]
        else:
            i+=1
    return a

def Funcs(a):
    global funs
    i=len(a)-1
    while i>-1:
        if(a[i] in funs.keys()):
            if(type(a[i+1])==float):
                a[i]=funs[a[i]](a.pop(i+1))
            else:
                i-=1
        else:
            i-=1

def MakeList(input):# Convert Strings to list containg number and opertators
    global funs
    ops=['/','*','+','-','(',')','^']
    # funs=['sin','cos','tan','csc','sec','cot','asin','acos','atan','acsc','asec','acot','hsin','hcos','htan','hcsc','hsec','hcot','ln,log']
    input = input.replace(" ", "")
    num=[]
    fun=[]
    opsList=[]
    for c in input:
        if(c in ops):
            if(len(fun)>0):
                if(''.join(fun) in funs):
                    opsList.append(''.join(fun))
                elif(fun[0]=='e'):
                    opsList.append(math.e)
                elif(fun==list('pi')):
                    opsList.append(math.pi)
            if(len(num)>0):
                opsList.append(getNum(''.join(num)))
            opsList.append(c)
            num=[]
            fun=[]
        elif(c.isdigit()):
            num.append(c)
        else:
            fun.append(c)
            if(''.join(fun) in funs):
                opsList.append(''.join(fun))
                fun=[]
            elif(fun[0]=='e'):
                opsList.append(math.e)
                fun=[]
            elif(fun==list('pi')):
                opsList.append(math.pi)
                fun=[]
    if(len(num)>0):
        opsList.append(getNum(''.join(num)))
    if(len(fun)>0):
        if(''.join(fun) in funs):
            opsList.append(''.join(fun))
        elif(fun[0]=='e'):
            opsList.append(math.e)
        elif(fun==list('pi')):
            opsList.append(math.pi)
    return opsList

def Calculate(input):#Main Function
    input=MakeList(input)
    Brac(input)
    print(input)
    Brac(input)
    return AllOperator(input)[0]

# print((((2-2+1)*(1+1)*7))-2+2-9*2*(4+(5*(8+5*(1*1+4)))))
# a="(((2-2+1)*(1+1)*7))-2+2-9*2*(4+(5*(8+5*(1*1+4))))"

# a="(sin30+cos30*(sin30+sin(30*cos50)))"
# print(Calculate(a))
# print("21".isdigit())