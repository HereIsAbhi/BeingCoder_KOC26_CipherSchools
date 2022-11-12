# x= lambda n1,n2: n1+n2
# print(x(3,4))
a= int(input("a:"))    
b= int(input("b:"))
def add(n1,n2):
    sum= n1+n2
    return sum
def sub(n1,n2):
    sub= n1-n2
    return sub    
def prod(n1,n2):
    prod= n1*n2
    return prod   
def div(n1,n2):
    div= n1/n2
    return div  

user=input("")
if user == "addition"or user=="add":
   print ("addition:",add(a,b))
elif user == "substraction"or user=="sub":
  print ("sub:",sub(a,b))
elif user == "product"or user=="prod":  
  print ("prod:",prod(a,b))
elif user == "divide"or user=="div":  
  print ("div:",div(a,b))


