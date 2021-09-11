
p1 = [30, 15]
p2 = [20, 10]
p3 = [10, 15]
p4 = [7, 3]
p5 = [2, 5]
t1 = [0, 0, 20, 0, 10, 30]
t2 = [24, 6, 32, 12, 22, 15]

#p is the list of points..
p = [p1, p2, p3, p4, p5]

#t is the list of triangles..
t = [t1, t2]

def triangleArea(x1, y1, x2, y2, x3, y3):
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1)  
                + x3 * (y1 - y2)) / 2.0)

#x1, y1, x2, y2, x3, y3, x, y
def isInside(T, P):   
    # Calculate area of bigger triangle 
    A = triangleArea (T[0], T[1], T[2], T[3], T[4], T[5]) 

    # Calculate area of triangle PBC  
    A1 = triangleArea (P[0], P[1], T[2], T[3], T[4], T[5]) 
      
    # Calculate area of triangle PAC  
    A2 = triangleArea (T[0], T[1], P[0], P[1], T[4], T[5]) 
      
    # Calculate area of triangle PAB  
    A3 = triangleArea (T[0], T[1], T[2], T[3], P[0], P[1]) 
      
    # Check if sum of A1, A2 and A3  
    # is same as A 
    if(A == A1 + A2 + A3): 
        return True
    else: 
        return False

def validatePoints(t, p):
    for i in t:
        for j in p:
            print("For triangle :", i, end = " ")
            print("Point ",j, " lies: ", end = " ")
            if(isInside(i, j)):
                print("Inside")
            else:
                print("Outside")

validatePoints(t, p)
            
