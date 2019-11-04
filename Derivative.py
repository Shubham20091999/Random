import math
import sys

class Calc:
    __ops=['/','*','+','-','^']
    __brs=['(',')']
    __fns={'sin':math.sin,'cos':math.cos,'tan':math.tan,'asin':math.asin,'acos':math.acos,'atan':math.atan,'hsin':math.sinh,'hcos':math.cosh,'htan':math.tanh,'ln':math.log,'log':math.log10}

    def __init__(self,op,l,r,m=1):
        self.operation=op
        self.left=l
        self.right=r
        self.m=m
    def MakeItConst(self,c):
        self.operation=None
        self.left=c
        self.right=None
    def MakeItOp(self,op,l,r):
        self.operation=op
        self.left=l
        self.right=r
    def MakeItFn(self,fn,r):
        self.operation=fn
        self.left=None
        self.right=r

    @staticmethod
    def const(c,m=1):
        return Calc(None,c,None,m)

    @staticmethod
    def fn(f,c,m=1):
        return Calc(f,None,c,m)

    @staticmethod
    def op(o,l,r,m=1):
        return Calc(o,l,r,m)
    
    def __repr__(self):
        if(self.operation==None):
            if(self.m==1):
                return str(self.left)
            else:
                return '-'+str(self.left)
        if(self.m==-1):
            if(self.left==None):
                return self.operation+'('+'-'+str(self.right)+')'
            else:
                return '('+str(self.left)+self.operation+'-'+str(self.right)+')'
        else:
            if(self.left==None):
                return self.operation+'('+str(self.right)+')'
            else:
                return '('+str(self.left)+self.operation+str(self.right)+')'

    def __str__(self):
        if(self.operation==None):
            if(self.m==1):
                return str(self.left)
            else:
                return '-'+str(self.left)
        if(self.m==-1):
            if(self.left==None):
                return self.operation+'('+'-'+str(self.right)+')'
            else:
                return '('+str(self.left)+self.operation+'-'+str(self.right)+')'
        else:
            if(self.left==None):
                return self.operation+'('+str(self.right)+')'
            else:
                return '('+str(self.left)+self.operation+str(self.right)+')'

    def WhatIsit(self):
        if(self.operation==None):
            return 'C'
        elif(self.left==None):
            return 'F'
        else:
            return 'O'

    def MakeEqualTo(self,other):
        self.right=other.right
        self.left=other.left
        self.operation=other.operation
        self.m=other.m

    @staticmethod       
    def __getFun(a,unk):
        if(''.join(a) in Calc.__fns.keys()):
            return ''.join(a)
        elif(a[0]=='e'):
            return math.e
        elif(a==['p','i']):
            return math.pi
        elif(a[0] in unk):
            return a[0]
        return None

    @staticmethod
    def __getNum(a):#Get Number if input is Number str
        try:
            return Calc.const(float(a))
        except:
            t=a.split('.')
            return Calc.const(float(t[0])+float(t[1])/pow(10,len(t[1])))
    
    @staticmethod
    def __Break(input,unk=[]):
        input=input.replace(" ",'')
        tnum=[]
        tfn=[]
        output=[]
        for c in input:
            if(c in Calc.__brs or c in Calc.__ops):
                if(len(tfn)>0):
                    output.append(Calc.__getFun(tfn,unk))
                    tfn=[]
                elif(len(tnum)>0):
                    output.append(Calc.__getNum(''.join(tnum)))
                    tnum=[]
                output.append(c)
            elif(c.isdigit()):
                tnum.append(c)
            else:
                tfn.append(c)
                tmp=Calc.__getFun(tfn,unk)
                if(tmp!=None):
                    if(tmp in unk):
                        output.append(Calc.const(tmp))
                    else:
                        output.append(tmp)
                    tfn=[]
        if(len(tfn)>0):
            output.append(Calc.__getFun(tfn,unk))
        elif(len(tnum)>0):
            output.append(Calc.__getNum(''.join(tnum)))
        return output

    @staticmethod
    def __CheckNum(a,unk):
        t=type(a)
        if(t==Calc or t==float or t==int):
            return True
        if(a in unk):
            return True
        return False

    @staticmethod
    def __ParseOp(input,op,unk=[]):
        i=0
        while i<len(input):
            if(input[i] in op):
                m=1
                temp=input[i]
                if(input[i+1]=='-'):
                    m=-1
                    input.pop(i)
                if(Calc.__CheckNum(input[i+1],unk) and Calc.__CheckNum(input[i-1],unk)):
                    input[i-1]=Calc.op(temp,input[i-1],input[i+1],m)
                del input[i:i+2]
                continue
            i+=1
        return input

    @staticmethod 
    def __ParseFn(input,unk):
        i=len(input)-1
        while i>-1:
            if(input[i] in Calc.__fns.keys()):
                m=1
                if(input[i+1]=='-'):
                    m=-1
                    input.pop(i+1)
                if(Calc.__CheckNum(input[i+1],unk)):
                    input[i]=Calc.fn(input[i],input[i+1],m)
                    input.pop(i+1)
            else:
                i-=1
        return input
                    

    @staticmethod
    def __ParseAllOp(input,unk):
        Calc.__ParseFn(input,unk)
        Calc.__ParseOp(input,['^'],unk)
        Calc.__ParseOp(input,['*','/'],unk)
        if(input[0]=='-'):
            input.pop(0)
            input[0]*=-1
        Calc.__ParseOp(input,['+','-'],unk)
        return input

    @staticmethod
    def __Parseit(a,unk):
        lbrac=[]
        i=0
        while i<len(a):
            if(a[i]=='('):
                lbrac.append(i)
            elif(a[i]==')'):
                ll=lbrac.pop(-1)
                val=Calc.__ParseAllOp(a[ll+1:i],unk)[0]
                del a[ll+1:i+1]
                a[ll]=val
                i=ll
            i+=1

    @staticmethod
    def GetParsedEquation(string,unk=[]):
        input=['(']+Calc.__Break(string,unk)+[')']
        Calc.__Parseit(input,unk)
        return input[0]

    @staticmethod
    def EvaluateParsed(input,vals={}):
        if(input.WhatIsit()=='C'):
            try:
                return vals[input.left]
            except:
                return input.left
        if(input.WhatIsit()=='O'):
            l=Calc.EvaluateParsed(input.left,vals)
            r=Calc.EvaluateParsed(input.right,vals)
            if(input.operation=='^'):
                return pow(l,input.m*r)
            elif(input.operation=='/'):
                return input.m*l/r
            elif(input.operation=='*'):
                return input.m*l*r
            elif(input.operation=='+'):
                return l+input.m*r
            elif(input.operation=='-'):
                return l-input.m*r
        if(input.WhatIsit()=='F'):
            v=Calc.EvaluateParsed(input.right,vals)
            return Calc.__fns[input.operation](v)
        
class DerFn:
    @staticmethod
    def sin(c):
        return Calc.fn("cos",c,1)
    @staticmethod
    def cos(c):
        return Calc.fn("sin",c,-1)
    @staticmethod
    def tan(c):
        t1=Calc.fn("cos",c,1)
        return Calc.op("^",t1,2,-1)
    @staticmethod
    def ln(c):
        return Calc.op('/',1,c)
    @staticmethod
    def log(c):
        return Calc.op('/',math.log10(math.e),c)
    @staticmethod
    def asin(c):
        t1=Calc.op('-',1,Calc.op('^',c,2))
        t2=Calc.op('^',t1,0.5)
        return Calc.op('/',1,t2)
    @staticmethod
    def acos(c):
        t1=Calc.op('-',1,Calc.op('^',c,2))
        t2=Calc.op('^',t1,0.5)
        return Calc.op('/',-1,t2)
    @staticmethod
    def atan(c):
        t1=Calc.op('+',1,Calc.op('^',c,2))
        return Calc.op('/',1,t1)
    @staticmethod
    def hsin(c):
        return Calc.fn('hcos',c)
    @staticmethod
    def hcos(c):
        return Calc.fn('hsin',c)
    @staticmethod
    def htan(c):
        return Calc.op('^',Calc.fn('hcos',c),-2)

derFn={'sin':DerFn.sin,'cos':DerFn.cos,'tan':DerFn.tan,'ln':DerFn.ln,'log':DerFn.log,'asin':DerFn.asin,'acos':DerFn.acos,'atan':DerFn.atan,'hsin':DerFn.hsin,'hcos':DerFn.hcos,'htan':DerFn.htan}


def DerivativeParsed(c,var):
    if(c.WhatIsit()=='C'):
        if(c.left==var):
            return Calc.const(1)
        return Calc.const(0)
    if(c.WhatIsit()=='O'):
        if(c.operation=='*'):
            t1=Calc.op('*',DerivativeParsed(c.left,var),c.right)
            t2=Calc.op('*',DerivativeParsed(c.right,var),c.left)
            return Calc.op('+',t1,t2)
        elif(c.operation=='+'):
            return Calc.op('+',DerivativeParsed(c.left,var),DerivativeParsed(c.right,var))
        elif(c.operation=='-'):
            return Calc.op('-',DerivativeParsed(c.left,var),DerivativeParsed(c.right,var))
        elif(c.operation=='^'):
            t1=Calc.op('-',c.right,Calc.const(1))
            t2=Calc.op('^',c.left,t1)
            p1=Calc.op('*',c.right,DerivativeParsed(c.left,var))
            q1=Calc.fn('ln',c.left)
            q2=Calc.op('*',q1,c.left)
            q3=Calc.op('*',q2,DerivativeParsed(c.right,var))
            r1=Calc.op('+',q3,p1)
            return Calc.op('*',t2,r1)
        elif(c.operation=='/'):
            t1=Calc.op('*',DerivativeParsed(c.left,var),c.right)
            p1=Calc.op('*',DerivativeParsed(c.right,var),c.left)
            r1=Calc.op('-',t1,p1)
            return Calc.op('/',r1,Calc.op('^',c.right,Calc.const(2)))
    elif(c.WhatIsit()=='F'):
        return Calc.op('*',derFn[c.operation](c.right),DerivativeParsed(c.right,var))
    else:
        return Calc.const(0)

                
def Simplify(input,vars=[]):
    if(input.WhatIsit()=='C'):
        return
    if(input.WhatIsit()=='O'):
        Simplify(input.left,vars)
        Simplify(input.right,vars)
        l=False
        r=False
        lc=False
        rc=False
        if(input.left.WhatIsit()=='C'):
            lc=True
            if(input.left.left==0):
                l=True 
        if(input.right.WhatIsit()=='C'):
            rc=True
            if(input.right.left==0):
                r=True      
        if(l or r):
            if(input.operation=='^'):
                if(l and r):
                    print("Error")
                    sys.exit()
                if(l):
                    input.MakeItConst(0)
                elif(r):
                    input.MakeItConst(1)
            elif(input.operation=='/'):
                if(r):
                    print("Error")
                    sys.exit()
                if(l):
                    input.MakeItConst(0)
            elif(input.operation=='*'):
                input.MakeItConst(0)
            elif(input.operation=='+'):
                if(l and r):
                    input.MakeItConst(0)
                elif(l):
                    input.MakeEqualTo(input.right)
                elif(r):
                    input.MakeEqualTo(input.left)    
            elif(input.operation=='-'):
                if(l and r):
                    input.MakeItConst(0)
                elif(l):
                    input.MakeEqualTo(input.right)
                    input.m=-1
                elif(r):
                    input.MakeEqualTo(input.left)
        elif(lc and rc):
            if(input.left.left not in vars and input.right.left not in vars):
                input.MakeItConst(Calc.EvaluateParsed(input))
    elif(input.WhatIsit()=='F'):
        Simplify(input.right,vars)
        if(input.right.WhatIsit()=='C'):
            if(input.right.left not  in vars):
                try:
                    input.MakeItConst(Calc.EvaluateParsed(input))
                except:
                    return


a='sin(0)'
p=Calc.GetParsedEquation(a)
Simplify(p)
print(p)
        





