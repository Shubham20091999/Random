import math

def distance(a,b):#Finding Distance
    distSq=0
    for i in range(0,len(a)):
        distSq+=(pow((a[i]-b[i]),2))
    return math.sqrt(distSq)

def CheckBetween(x,a,b):#Check if x is between a and b
    if(x==-1):
        return False
    if(a[0]>b[0]):
        (a[0],b[0])=(b[0],a[0])
    if(a[0]<=x[0] and x[0]<=b[0]):
        return True
    return False

def InterSectionPoint(dot,a,b,add):#Getting the point of intersection
    m=0
    m+=add
    (cy,cx,c)=(1,-m,dot[1]-m*dot[0])#Coeff of the line passing througn the given points and Slope m
    (c1y,c1x,c1)=(a[0]-b[0],-(a[1]-b[1]),b[1]*a[0]-a[1]*b[0])#Coeff of the line passing through two points given

    det=c1x*cy-cx*c1y#Det to check if intersection exists
    if(det==0):#Checking the determinent
        return -1
        
    (xi,yi)=((cy*c1-c1y*c)/det,(-cx*c1+c1x*c)/det)
    #The point of intersection
    
    return (xi,yi)#Returning the point of intersection
        
def CheckInside(dot,pts,checks):
    count=0#Counting the points of intersection on the left
    add=0
    change=math.tan(math.pi/(2*checks))
    for i in range(0,checks):
        for i in range(0,len(pts)):
            (a,b)=(pts[i-1],pts[i])#Cycling through the points of intersection
            
            Ipt=InterSectionPoint(dot,a,b,add)#intersection Point
            if(Ipt==-1 or not(CheckBetween(Ipt,a,b))):
                continue#If intersection point is not between the points a and b
            if(Ipt[0]<dot[0]):#counting the left count 
                count+=1
            elif(Ipt[0]==dot[0]):
                return True#if the point is on the Polygon
        
        if(count%2!=0):#if Count is multiple of 2 point is outside
            return True
        
        add+=change
    return False#if Count is not a multiple of 2 point is outside
