

n1= int(input("n1:"))
n2= int(input("n2:"))
for i in range(n1,n2+1):
    for j in range(2,int(i/2)+1):
        if i%j==0:
           break

    else:
         print(i)
         