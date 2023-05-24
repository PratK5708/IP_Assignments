def RAT(n):
  for i in range(1,n+1):
      for j in range(0,i):
         print(j+1,end=" ")
      print()


def IsT(n):
  for i in range(1,n+1):
    for j in range(n,i,-1):
      print("  ",end="")
    for k in range(1,i+1):
      print(k,end="")
    for l in range(i-1,0,-1):
      print(l,end="")
    print()

def kite(n):
  while 0<n:
    print((n-1)*"*",end=" ")
    a=1
    for  i in range(1,n+1):
     print(i,end="") 
    n=n-1
    a=a+2
    print()

def halfk(n):
   for i in range(n):
      for j in range(1,i):
         print(j,end=' ')
      print()
   for i in range(n,0, -1):
      for k in range(1,i+1):
         print(k,end=' ')
      print()

def x(n):
  for i in range(n,0,-1):
      for j in range(n-i):
          print(" ", end=" ")
      for k in range(1,i*2):
          print(k, end="")
      print()
  for i in range(2,n+1):
      for j in range(n-i):
          print(" ", end=" ")
      for j in range(1,2*i):
          print(j, end="")
      print()



print("1. Right-angled triangle")
print("2. Iscosceles triangle")
print("3. Kite")
print("4. Half Kite")
print("5. X")
q=int(input("Enter the operation you need to execute: "))
n=int(input("The value till to be execute: "))
if q==1:
  RAT(n)
  
elif q==2:
   if n%2!=0:
    print("Operation only works on even number")
   else:
    IsT(n)
    
elif q==3:
   if n%2!=0:
    print("Operation only works on even number")
   else:
    kite(n)
    
elif q==4:
  halfk(n)
  
elif q==5:
  x(n)
else:
  print("Incorrect operation choosen")
  
       

  
  

