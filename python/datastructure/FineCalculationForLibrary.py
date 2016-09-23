rd, rm, ry = [int(x) for x in input().split(' ')]
ed, em, ey = [int(x) for x in input().split(' ')]

if (ry, rm, rd) <= (ey, em, ed):
    print(0)
elif (ry, rm) == (ey, em):
    print(15 * (rd - ed))
elif ry == ey:
    print(500 * (rm - em))
else:
    print(10000)





actualReturn = [a for a in map(int, input().split(" "))]
expectedReturn = [a for a in map(int, input().split(" "))]
#print(actualReturn)
#print(expectedReturn)

aD = actualReturn[0]
aM = actualReturn[1]
aY = actualReturn[2]

eD = expectedReturn[0]
eM = expectedReturn[1]
eY = expectedReturn[2]

fine = 0

if aY <= eY and aM == eM and aD == eD:
    fine = 0
elif aY == eY and  aM == eM:
    fine = 15 *(aD - eD)
elif aY  == eY:
    fine = 500 *(aM-eM)
    
print(fine)   