# code to check leap year 
""" def checkyear(year):
    return(((year %4==0) and (year%100 != 0)) or (year%400==0));
year = int(input("enter year:"))
if (checkyear(year)):
    print("it is leap year")
else:
    print('no') """

"""year= int(input(""))
if(year%4==0):
       if(year%4!=0):
           print("leap")
       else : 
           if(year%400==0)
               print("leap")
           else:
               print("not") 
else:
        print("not leap")"""
"""year= int(input("enter year:"))
if(year%4==0):   
    if(year%100==0):
        if(year%400==0):
            print("leap")
        else:
            print("false")
    else:
        print("false")
else:
    print("false") """
from datetime import datetime,date
year= int(input("enter year:"))
month= int(input("enter month:"))
day=int(input("enter day:"))
hours=int(input("enter hours:"))
minutes=int(input("enter min:"))
secs=int(input("enter sec:"))


d= date(year,month,day)
print(d)
dt= datetime(year,month,day,hours,minutes,secs)
print(dt)



