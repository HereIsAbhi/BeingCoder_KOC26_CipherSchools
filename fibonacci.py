def fibo(num):
   for i in range(1,num+1):
       p=0
       q=1
       r= p+q
       s=str()
       s= str(p) + str(q) + str(r)
       
       p=q
       q=r
       print(s,end=" ")   
       

n = int(input("n:")  )
fibo(n)     
