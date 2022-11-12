import datetime

# d1 = int(input("enter d1:"))
# m1= int(input("enter M1:"))
# y1= int(input("enter y1:"))
# date= datetime.date(y1,m1,d1)
# d2 = int(input("enter d2:"))
# m2= int(input("enter M2:"))
# y2= int(input("enter y2:"))
# date1= datetime.date(y2,m1,d2)

# print("First date is:",date)
# print("Second date is:",date1)
# for i in range(y1,y2+1):
#     if (i%4==0 and i%100!=0) or i%400==0:
#         print(i,end=" ")
#         print("It is a leap year")
#     else:
#         print(i,end=" ")
#         print("It is not a leap year")    
#     i+=1    

# leap year method 2:
def ly(year1,year2):
    for i in range(year1,year2+1):
        if (i%4 ==0 and i%100!= 0 )or i%400==0:
            print(i,end=",")
        i+=1        
def notly(year1,year2):
    for i in range(year1,year2+1):
        if (i%4!=0 or i%100== 0) and i%400!=0:
            print(i,end=",")  
        i+=1                  

        
            
# # d1 = int(input("enter d1:"))
# # m1= int(input("enter M1:"))
y1= int(input("enter y1:"))
# # date= datetime.date(y1,m1,d1)
# # d2 = int(input("enter d2:"))
# # m2= int(input("enter M2:"))
y2= int(input("enter y2:"))
# # date1= datetime.date(y2,m2,d2)

# print("First date is:",date)
# # print("Second date is:",date1)
print("the leap year are: ")
ly(y1,y2)

print("\nthe non leap year are: ")
notly(y1,y2)







 

 

