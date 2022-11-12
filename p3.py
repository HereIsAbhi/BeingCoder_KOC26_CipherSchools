# code to multiply first_di8git and last_digit of a no;
def first_digit(n):
    while n>=10:
        n= n/10
    return int(n)
def last_digit(n):
    n= n%10
    return(n)

num= int(input("enter no:"))
f=first_digit(num)  
l=last_digit(num)  
print(f*l) 
print(f) 
print(l) 
        
