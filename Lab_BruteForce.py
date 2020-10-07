##Kyler Telge 1825829

#first equation#
a = int(input())
b = int(input())
c = int(input())

#second equation#
d = int(input())
e = int(input())
f = int(input())

def funct1(x,y):
    return a*x +b*y - c

def funct2(x,y):
    return d*x + e*y - f

for x in range(-10, 11):
    for y in range(-10, 11):
        if ((funct1(x,y) == funct2(x, y)) and funct1(x,y) == 0):
            print(x,y)
    if((funct1(x,y) == funct2(x, y)) and funct1(x,y) != 0):
        print('No solution')
