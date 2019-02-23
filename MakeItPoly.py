import sys

def MakePointsCyclic(l):#Make the points in all posible cyclic order
    new=[[l[0],l[1]]]
    temp=[]
    for i in range(2,len(l)):
        temp=[]
        for m in new:
            temp+=(Select(l[i],m))
        new=[]
        new=temp
    return new
        

def Select(x,l):#Give a point and a cyclic poly array and it will give back the polygon with this point added
    all=[]
    for i in range(0,len(l)):#checking intersection with all sides of poly so that we can add this point between two points
        ch1=CheckIntersectionInside(x,l[i],l)# checking intersection inside poly
        ch2=CheckIntersectionInside(x,l[i-1],l)# Checking intersection inside poly
        if(ch1 or ch2): # if any one gets intersected continue
            continue
        temp=PutAt(x,i,l)#Put new point between l[i] and l[i-1]
        all.append(temp)#Make an array with this point added
        
    return all#return the array


def PutAt(x,y,z):#putind value x at position y in list z
    l=z[:]
    s=len(l)
    k=l.append(l[s-1])
    if(y<0):
        return  l.append(x)
    for i in range(len(l)-1,y,-1):
        l[i]=l[i-1]
    l[y]=x
    return l

def CheckIntersectionInside(x,y,l):#Checking intersection of the line passing through point x and point y with polygon
    for i in range(0,len(l)):
        if(CheckIntersection(x,y,l[i],l[i-1])):
            return True
    return False

def CheckIntersection(x,y,a,b):#Checking intersection of line passing through point x and point y with line passing through point a and point b 
    if(x==y or b==a):
        sys.exit("Line from only one point cannot be made")

    (cy,cx,c)=(x[0]-y[0],-(x[1]-y[1]),y[1]*x[0]-x[1]*y[0])#making equation of line having passing through x and y
    
    (c1y,c1x,c1)=(a[0]-b[0],-(a[1]-b[1]),b[1]*a[0]-a[1]*b[0])#making equation of line having passing through a and b
    
    det=c1x*cy-cx*c1y

    if(det==0):
        return False
        
    if(x[0]>y[0]):
        (x,y)=(y,x)
    if(a[0]>b[0]):
        (a,b)=(b,a)
    
    if(det!=0):
        ptI=(xi,yi)=((cy*c1-c1y*c)/det,(-cx*c1+c1x*c)/det)
    
    return CheckBetween(ptI,a,b,x,y)#checking if the point of intersection is between given points or not
                                    #so that we can say that it is intersection poygon or not

def CheckBetween(x,a,b,p,q):#checking if the x lies between (a and b) and (p and q)
    if(a[0]>b[0]):
        (a,b)=(b,a)
    if(p[0]>q[0]):
        (p,q)=(q,p)
    if(a[0]<=x[0] and x[0]<=b[0] and p[0]<x[0] and x[0]<q[0]):
        return True

    if(a[1]>b[1]):
        (a,b)=(b,a)
    if(p[1]>q[1]):
        (p,q)=(q,p)
        
    if(a[1]<=x[1] and x[1]<=b[1] and p[1]<x[1] and x[1]<q[1]):
        return True
    
    return False
