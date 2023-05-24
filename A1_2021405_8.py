intial=int(input("Enter the intial ocst of thr car"))
DR=int(input("Enter the DR"))
depreciaiton=0.05*intial
M1=intial*0.01
cost=intial
U=50
Main=M1
for i in range(1,5+1):
   
   U=(U+(U*0.1))
   Value=U*6000
   
   
   cost=cost-(depreciaiton+Main)
   Main=M1+0.01*intial
   
   if Value>cost:
      print(i-1)
      break
   else:
      pass

for i in range(5,15+1):
   
   U=(U+(U*0.1))
   Value=U*6000
   
   
   cost=cost-(depreciaiton+Main)
   Main=M1+0.5*Main
   
   if Value>cost:
      print(i,("you will sell the car:"),i)
      break
   else:
      pass









     








     
