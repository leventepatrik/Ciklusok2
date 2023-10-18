import math
def szamok(szam1:float,szam2:float):
    i:int=math.floor(szam1) + 1
    while(i <= szam2):
        print(i,end=",")
        i+=1