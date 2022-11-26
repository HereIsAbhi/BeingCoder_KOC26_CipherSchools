import datetime


def leap_year(year1,year2):
    for i in range(year1,year2+1):
        if (i%4 ==0 and i%100!= 0 )or i%400==0:
            print(i,end=",")
        i+=1        
def non_leap_year(year1,year2):
    for i in range(year1,year2+1):
        if (i%4!=0 or i%100== 0) and i%400!=0:
            print(i,end=",")  
        i+=1                  

        
            
d1 = int(input("enter Date1:"))
m1= int(input("enter Month1:"))
y1= int(input("enter Year1:"))
date1= datetime.date(y1,m1,d1)
d2 = int(input("enter Date2:"))
m2= int(input("enter Month2:"))
y2= int(input("enter Year2:"))
date2= datetime.date(y2,m2,d2)

print("First date is:",date1)
print("Second date is:",date2)
print(" Leap years are: ")
leap_year(y1,y2)

print("\n Non leap years are: ")
non_leap_year(y1,y2)







 

 

