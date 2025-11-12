#fibricci sequence
num=int(input("enter the number"))
a,b=1,1
for i in range(num):#20 terms
   print(a,end=" ")
   a,b=b,a+b
