# code to find first_digit and last_digit
def first_digit(n):
# def is used to define a function
 while n>=10:
    n=n/10;
 return int(n)
n = int(input(""))
last_digit= n%10
print(first_digit(n))
print(last_digit)

