#Program developed by Sam Espana
#Program enhanced by Blong Lor 
#Date: 11/1/2025
import math
import os
print("Displaying current working directory (CWD) =",os.getcwd())

def udfCircumference(radius):
    return 2*math.pi*radius

def udfCircleArea(radius):
    return pow(radius,2)*math.pi

def udfRectangleArea(base,height):
    return base*height

def udfTriangleArea(base,height):
    return 0.5*base*height

def udfSquareArea(side):
    return pow(side,2)

def udfMenuOptions():
    print("HTC Corporation")
    print("1. Calculate the circumference of a circle")
    print("2. Calculate the area of a circle")
    print("3. Calculate the area of a rectangle")
    print("4. Calculate the area of a triangle")
    print("5. Calculate the area of a square")
    print("0. Enter a digit (1-5) to select menu option or Q to quit")
    return None

def main():
    wFile = open("Project4.txt", "a") #Using "a" to denote appending to txt file so it doesn't get rewritten

    udfMenuOptions()
    menuChoice = int(input("Enter menu choice (1-5) : "))
    if (menuChoice ==0):
        print("Have a nice day")
    elif (menuChoice ==1):
        print("Circumference = 2 x pi x radius")
        fltRadius = float(input("Enter radius : "))
        wFile.write(str(fltRadius)+"\n")
        wFile.write(str(udfCircumference(fltRadius))+"\n")
        #print("Circumference (formula) = ",2*math.pi*fltRadius)
        print("Circumference (function) =",udfCircumference(fltRadius))
    elif (menuChoice ==2):
        print("The area of a circle = radius x radius x pi")
        fltRadius = float(input("Enter radius : "))
        wFile.write(str(fltRadius)+"\n")
        wFile.write(str(udfCircleArea(fltRadius))+"\n")
        print("Area of circle (function) =",udfCircleArea(fltRadius))
    elif (menuChoice ==3):
        print("The area of a rectangle = base x height")
        fltBase = float(input("Enter base : "))
        fltHeight = float(input("Enter height : "))
        wFile.write(str(fltBase)+"  ")
        wFile.write(str(fltHeight)+"\n")
        wFile.write(str(udfRectangleArea(fltBase,fltHeight))+"\n")
        print("Area of rectangle (function) =",udfRectangleArea(fltBase,fltHeight))
    elif (menuChoice ==4):
        print("The area of a triangle = 1/2 x base x height")
        fltBase = float(input("Enter base : "))
        fltHeight = float(input("Enter height : "))
        wFile.write(str(fltBase)+"  ")
        wFile.write(str(fltHeight)+"\n")
        wFile.write(str(udfTriangleArea(fltBase,fltHeight))+"\n")
        print("Area of triangle (function) =",udfTriangleArea(fltBase,fltHeight))
    elif (menuChoice ==5):
        print("The area of a square = side x side, or side^2")
        fltSide = float(input("Enter side : "))
        wFile.write(str(fltSide)+"\n")
        wFile.write(str(udfSquareArea(fltSide))+"\n")
        print("Area of square (function) =",udfSquareArea(fltSide))
    else:
        print("Invalid menu option")

    wFile.close()
    print("Reading Project4.txt file")
    with open("Project4.txt") as rFile:
        data = rFile.read()
        print(data)


if __name__ == "__main__":
    main()
