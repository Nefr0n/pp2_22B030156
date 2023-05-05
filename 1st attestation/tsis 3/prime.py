n = int(input())
a = 0
if n > 1 : 
   for i in range(2,n): 
       if(n%i == 0): 
         a = 1 
         break  
else: 
  print("it is not a prime")  

if (a==0): 
  print(n, "is a prime nunber")
else: 
  print(n, "is not a prime number")