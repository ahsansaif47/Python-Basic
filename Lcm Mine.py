
lcm_List = []

def findNextPrime(prime):
    nxPrime = prime + 1
    i = 2
    while(i <= int(nxPrime/2)):
        if(nxPrime % i == 0):
            nxPrime+=1
            i = 2
        i+=1
    return nxPrime

def LCM(x, y):
    i = 2
    while(True):
        if((x % i == 0 or y % i == 0) or (x % i == 0 and y % i == 0)):
            lcm_List.append(i)
            if(x % i == 0 and y % i != 0):
                x = x / i
            elif(y % i == 0 and x % i != 0):
                y = y / i
            else:
                x = x / i
                y = y / i
                
        if(x%i != 0 and y%i != 0):
            i = findNextPrime(i)

        if(x == 1 and y == 1):
            break
        
    return lcm_List

def checkEvery_Integer(iList):
    for i in iList:
        if(int(i) != 1):
            return 0
    return 1;

prod = 1

x = eval(input("Enter the first number: "))
y = eval(input("Enter the second number: "))

LcmList = LCM(x, y)
print("LCM List is: ", LcmList)

for i in lcm_List:
    prod *= i

print("LCM is: ", prod)
