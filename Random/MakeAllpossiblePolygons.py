def CheckInBetween(ptA,ptC,ptD,m=False,c=False):
    if(ptA[1]-m*ptA[0]-c==0 or m==False):
        if((ptA[0]<ptD[0] and ptA[0]<ptC[0])):
            return False
        if((ptA[0]>ptD[0] and ptA[0]>ptC[0])):
            return False
        if((ptA[1]<ptD[1] and ptA[1]<ptC[1])):
            return False
        if((ptA[1]>ptD[1] and ptA[1]>ptC[1])):
            return False
        return True
    else:
        return False


def IntersectionChecKWithLines(ptA,ptB,ptC,ptD):
    if((ptA[0]-ptB[0])!=0):
        m1=(ptA[1]-ptB[1])/(ptA[0]-ptB[0])
    else:
        m1=float('inf')
    
    if((ptC[0]-ptD[0])!=0):
        m2=(ptC[1]-ptD[1])/(ptC[0]-ptD[0])
    else:
        m2=float('inf')
    
    c1=-ptA[0]*m1+ptA[1]
    c2=-ptC[0]*m2+ptC[1]
    
    if(m1==m2):
        if(CheckInBetween(ptA,ptC,ptD,m2,c2)):
            return True
        else:
            return False
    
    if(m1!=float('inf') and m2!=float('inf')):
        ptI=((c2-c1)/(m1-m2),(c1*m2-m1*c2)/(m2-m1))
    else:
        if(m1==float('inf')):
            ptI=(ptA[0],c2)
        else:
            ptI=(ptC[0],c1)
    if(CheckInBetween(ptI,ptC,ptD) and CheckInBetween(ptI,ptA,ptB)):
        return True
    return False

def IntersectionCheckWithPoly(ptA,Poly):
    if(len(Poly)<=2):
        return False
    ptB=Poly[-1]
    for i in range(0,len(Poly)-2):
        if(IntersectionChecKWithLines(ptA,ptB,Poly[i],Poly[i+1])):
            return True
    return False

def IntersectionCheckWithPolyForward(ptA,Poly):
    if(len(Poly)<=2):
        return False
    ptB=Poly[0]
    for i in range(1,len(Poly)-1):
        if(IntersectionChecKWithLines(ptA,ptB,Poly[i],Poly[i+1])):
            return True
    return False

def MakeAllPoly(list,poly,Ans=False):
    i=0
    while i<len(list):
        if(IntersectionCheckWithPoly(list[i],poly)):
            i+=1
            continue
            
        poly.append(list.pop(i))
    
        if(len(list)==0):
            if(IntersectionCheckWithPolyForward(poly[-1],poly[0:-1])):
                return
            if(Ans==False):
                print(poly)
            else:
                Ans.append(poly)
            return

        MakeAllPoly(list[:],poly[:],Ans)
        list.insert(i,poly.pop())
        i+=1
def MakePolyStartingFrom(list,index=0,Ans=False):
    n=list[0:index]+list[index+1:len(list)]
    MakeAllPoly(n,[list[index]],Ans)

def Area(_poly):
    left=0
    right=0
    poly=_poly+[_poly[0]]
    for i in range(0,len(poly)-1):
        left+=poly[i][0]*poly[i+1][1]
        right+=poly[i][1]*poly[i+1][0]
    return abs(left-right)/2

def polyWithMaxArea(poly):
    Ans=[]
    MakePolyStartingFrom(poly,0,Ans)
    max_Area=0
    max_poly=[]
    for i in range(0,len(Ans)):
        area=Area(Ans[i])
        if(area>max_Area):
            max_Area=area
            max_poly=Ans[i]

    return (max_poly,max_Area)

def polyWithMinArea(poly):
    Ans=[]
    MakePolyStartingFrom(poly,0,Ans)
    min_area=float('inf')
    min_poly=[]
    for i in range(0,len(Ans)):
        area=Area(Ans[i])
        if(area<min_area):
            min_area=area
            min_poly=Ans[i]
    return (min_poly,min_area)

o=[(-2,0),(-1,1),(1,0),(2,0),(1,-1),(-1,0)]
print(polyWithMinArea(o))

# o=[(4,10),(9,7),(11,2),(2,2)]
# print(Area(o))
# poly=[(-2, 0), (-1, 1), (1, 0), (2, 0), (1, -1)]
# print(IntersectionChecKWithLines((-1, 1),(1,0),(2,0),(-1,0)))
