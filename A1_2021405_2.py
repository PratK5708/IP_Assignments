n=int(input("Enter the number of the student: "))
def sq():
   s=int(input("Enter the side of the square: "))
   p=4*s
   a=s*s
   print("Perimeter of Square:",p)
   print("Area of Square:",a)

def rec():
   l=int(input("Enter the length for the rectangle:"))
   b=int(input("Enter the breadth for the rectangle:"))
   p=2*(l+b)
   a=l*b
   print("Perimeter of Rectangle:",p)
   print("Area of Rectangle:",a)
   
def rho():
   l=int(input("Enter the length for the Rhombus:"))
   d1=int(input("Enter the diagonal 1:"))
   d2=int(input("Enter the diagonal 2:"))
   p=4*l
   a=(d1*d2)*0.5
   print("Perimeter of Rhombus:",p)
   print("Area of Rhombus:",a)

def llgm():
   l=int(input("Enter the height for the parallelogram:"))
   b=int(input("Enter the height for the parallelogram:"))
   h=int(input("Enter the side_1:"))
   p=2*(l+b)
   a=b*h
   print("Perimeter of parallelogram:",p)
   print("Area of parallelogram:",a)

def cir():
   r=int(input("Enter the radius of the circle:"))
   p=2*(3.14)*r
   a=(3.14)*r*r
   print("Circumference of the circle:",p)
   print("Area of circle:",a)



def cube():
      s=int(input("Enter side of the cube"))
      lsa=4*s*s
      tsa=6*s*s
      v=s*s*s
      print("Lateral surface area:",lsa)
      print("Curved surface area:",tsa)
      print("Lateral saurface area:",v)

def cubiod():
   l=int(input("Enter length of the cube"))
   h=int(input("Enter height of the cube"))
   b=int(input("Enter breadth of the cube"))
   lsa=2*h*(l+b)
   tsa=2*(l*b+h*l+b*h)
   v=l*b*h
   print("Lateral surface area:",lsa)
   print("Curved surface area:",tsa)
   print("Lateral saurface area:",v)

def cone():
   l=int(input("Enter length of the cube"))
   r=int(input("Enter height of the cube"))
   h=int(input("Enter breadth of the cube"))
   lsa=(3.14)*r*l
   tsa=(3.14)*r*(l+r)
   v=(0.33)*(3.14)*r*r*h
   print("Lateral surface area:",lsa)
   print("Curved surface area:",tsa)
   print("Lateral saurface area:",v)
   

def hem():
   r=int(input("Enter height of the cube"))
   lsa=2*(3.14)*r*r
   tsa=3*(3.14)*r*r
   v=(0.666)*(3.14)*r*r*r
   print("Lateral surface area:",lsa)
   print("Curved surface area:",tsa)
   print("Lateral saurface area:",v)

def sph():
   r=int(input("Enter height of the cube"))
   lsa=4*(3.14)*r*r
   tsa=4*(3.14)*r*r
   v=1.33*(3.14)*r*r*r
   print("Lateral surface area:",lsa)
   print("Curved surface area:",tsa)
   print("Lateral saurface area:",v)

def scyl():
   r=int(input("Enter height of the cube"))
   h=int(input("Enter height of the cube"))
   lsa=2*(3.14)*r*h
   tsa=2*(3.14)*r*(r+h)
   v=(3.14)*r*r*h
   print("Lateral surface area:",lsa)
   print("Curved surface area:",tsa)
   print("Lateral saurface area:",v)

def hcyl():
   R1=int(input("Enter height of the cube"))
   R2=int(input("Enter height of the cube"))      
   h=int(input("Enter height of the cube"))
   lsa=2*(3.14)*h*(R1+2)
   tsa=2*(3.14)*((R1+R2)+((R1**2)-(R2**2)))
   v=(3.14)*(R1**2-R2**2)*h
   print("Lateral surface area:",lsa)
   print("Curved surface area:",tsa)
   print("Lateral saurface area:",v)

choice=int(input("Enter the dimension [0-->2D, 1--> 3D & Exit-->2 ]:"))
if choice==0:
   print(" 1._for Sqaure")
   print(" 2._for Rectangle")
   print(" 3._for Rhombus")
   print(" 4._for Parallelogram")
   print(" 5._for circle")
   c=int(input("Enter the corresponding serial number"))
   if c==1:
      print("You chose square")
      sq()
   elif c==2:
      print("You chose rectangle")
      rec()
   elif c==3:
      print("You chose rhombus")
      rho()
   elif c==4:
      print("You chose parllelogram")
      llgm()
   elif c==5:
      print("You chose circle")
      cir()
   else:
      pass
elif choice==1:
         print(" 1._for Cube")
         print(" 2._for Cubiod")
         print(" 3._for Right circular cone")
         print(" 4._for Hemisphere")
         print(" 5._for Sphere")
         print(" 6._for Solid Cylinder ")
         print(" 7._for Hollow Cylinder")
         
         c=int(input("Enter the corresponding serial number"))
         if c==1:
            print("You chose cube")
            cube()
         elif c==2:
            print("You chose Cubiod")
            cubiod()
         elif c==3:
            print("You chose Right circular cone")
            hem()
         elif c==4:
            print("You chose hemisphere")
            sph()
         elif c==5:
            print("You chose sphere")
            scyl()
         elif c==6:
            print("You chose solid cylinder")
            hcyl()
         else:
            pass
elif choice==2:
   print("Exit")
   pass
         
         
         
         
         

   



   

   
   





  

    
   
