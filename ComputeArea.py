import math


def inputData():
    global radius
    radius = float(input('Enter the radius of circle in centimeters: '))


def calcArea():
    global circleArea
    circleArea = math.pi * pow(radius, 2)


def printData():
    print("The area of circle with radius " + str(radius) + " is " + format(circleArea, ".2f") + " sq. cm.")


def main():
    print('Compute Area Program')
    print('This program is designed to compute area of the circle.')
    inputData()
    calcArea()
    printData()


main()
