import math
from math import pi,sqrt,radians,degrees
import sys

g=9.8
G=6.67e-11
e=1.6021917e-19
ke=8.9875e9
me=9.1095e-31
mp=1.67261e-27
mn=1.674929e-27

blocked=["exec","sys","eval","PROCESS","CMD","RESULT","block","import","math","from",]

def sin(deg):
    return math.sin(radians(deg))
def cos(deg):
    return math.cos(radians(deg))
def tan(deg):
    return math.tan(radians(deg))
def asin(n):
    return degrees(math.asin(n))
def acos(n):
    return degrees(math.acos(n))
def atan(n):
    return degrees(math.atan(n))
def sq(n):
    return n*n

ans=0

def PROCESS(CMD):
    global ans
    
    for block in blocked:
        if block in CMD:
            print('The keyword "'+block+'" has been blocked for security reasons.')
            return

    RESULT=eval(CMD)
    
    if type(RESULT).__name__=="float" and abs(RESULT)>=1e-3 and abs(RESULT)<=1e9:
        print("%.6f"%RESULT)
    elif type(RESULT).__name__=="float" and abs(RESULT)>=1e9:
        print("%e"%RESULT)
    else:
        print(RESULT)

    ans=RESULT
           
print("Welcome to YAXO Physics Calculator!\n")
while True:
    try:
        PROCESS(input(">>> "))
    except KeyboardInterrupt:
        break
    except:
        print(sys.exc_info()[0].__name__)

input("\nThank you for using YAXO Physics Calculator! (Press Return to exit)")
