# import sys
# sys.setrecursionlimit(1200)

# def name():
#   print("Hello world")
#   name()
#   print(sys.getrecursionlimit())
  
# name()  
# def sum_recursion(num):
#     if num==0:
#         return 0
#     return num + sum_recursion(num-1)

# print(sum_recursion(5))  

# def factorial(num):
#     if num == 0 :
#        return 1
#     return num*factorial(num-1)

# n = int(input("enter:"))    
# print(factorial(n)) 

# a= int(input(""))
# p=0
# q=1
# print(p)
# print(q)
# for i in (0,a+1):
#     r= p+q
#     print(r)
#     p=q
#     q=r
a=int(input("Enter the terms"))
f=0                                         #first element of series
s=1                                         #second element of series
if a<=0:
    print("The requested series is
",f)
else:
    print(f,s,end=" ")
    for x in range(2,a):
        next=f+s                           
        print(next,end=" ")
        f=s
        s=next
    


