print("Hey there, Welcome to the appliation. Please select one of the following operaiton:")
print("1. Find reverse of a number:")
print("2.Check whether a number is a palindrome or not.:")
print("3.Check wheter a number is a Narcissistic number or not.:")
print("4. Find the sum of digits of a number:")
print("5. Find the sum of square of digits of a numebr:")
print("6. Select 6 to exit the application:")
print(" ")

p=int(input("Enter the above choice to choose the operation:"))
 
n=input("Enter any non negative number:")

def getReverse(n):
   a=len(n)
   b=""
   
   for i in range(a,0,-1):
      if n[i-1]==0:
         pass
      else:
         b+=n[i-1]
   print("Reversed number: " ,b)
      
def checkPalindrome(n):#1221
   a=n[::-1]
   if n==a:
      print("True")
   else:
      print("False")

def findDigitSum(n):
   l=[]
   for i in n:
      l.append(int(i))
   a=sum(l)
   print(a)
   
def findSquareDigitSum(n):
   l=[]
   for i in n:
      l.append(int(i)**2)
   a=sum(l)
   print("Sum of the square digits",a)

def checkNarcissisitic(n):
   l=[]
   z=str(n)
   a=len(z)
   for i in z:
      l.append(int(i)**a)
   b=sum(l)
   
   if n==str(b):
      print("True")
   else:
      print("False")

if p==1:
   getReverse(n)
elif p==2:
   checkPalindrome(n)
elif p==3:
   checkNarcissisitic(n)
elif p==4:
   findDigitSum(n)
elif p==5:
   findSquareDigitSum(n)
else:
   pass
   
   
   

   


   
