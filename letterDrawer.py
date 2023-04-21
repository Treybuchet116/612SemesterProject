import turtle as t
import math



def setLetterRadius(OUTERRADIUS, NUMCONSONANTS):
    if NUMCONSONANTS == 1:
        return OUTERRADIUS * .66
    elif NUMCONSONANTS == 2 or NUMCONSONANTS == 3:
        return OUTERRADIUS * .4
    elif NUMCONSONANTS == 4 or NUMCONSONANTS == 5:
        return (OUTERRADIUS * 1.3) / NUMCONSONANTS
    else:
        return (OUTERRADIUS * 1.5) / NUMCONSONANTS


def drawOuterCircle():
    OUTERRADIUS = 200
    EAST = 0
    NORTH = 90
    WEST = 180
    SOUTH = 270

    outerRing = t.Turtle()
    outerRing.width(6)
    outerRing.hideturtle()
    outerRing.penup()
    outerRing.speed(0)
    outerRing.seth(SOUTH)
    outerRing.forward(OUTERRADIUS)
    outerRing.seth(EAST)
    outerRing.pendown()
    outerRing.circle(OUTERRADIUS)

def drawTypeOne(letterRing, marker, TYPEONEDISTANCE, LETTERRADIUS, double):
    A = 200
    B = 200 + (LETTERRADIUS / 20) - LETTERRADIUS
    C = LETTERRADIUS
    neededCosine = (B**2 + A**2 - C**2) / (2*A*B)
    neededAngle = (math.degrees(math.acos(neededCosine)))

    letterRing.forward(TYPEONEDISTANCE)
    letterRing.left(90)
    letterRing.pendown()
    letterRing.circle(LETTERRADIUS)
    if double == True:
        letterRing.penup()
        letterRing.left(90)
        letterRing.forward(20)
        letterRing.right(90)
        letterRing.pendown()
        letterRing.circle(LETTERRADIUS - 20)

    

    marker.left(neededAngle)
    marker.forward(200)
    marker.pendown()
    marker.forward(10)
    marker.penup()
    marker.backward(210)
    marker.right(neededAngle * 2)
    marker.forward(200)
    marker.pendown()
    marker.forward(10)




def drawTypeTwo(letterRing, TYPETWODISTANCE, LETTERRADIUS, double):
    letterRing.forward(TYPETWODISTANCE)
    letterRing.left(90)
    letterRing.pendown()
    letterRing.circle(LETTERRADIUS)
    if double == True:
        letterRing.penup()
        letterRing.left(90)
        letterRing.forward(20)
        letterRing.right(90)
        letterRing.pendown()
        letterRing.circle(LETTERRADIUS - 20)

def drawTypeThree(letterRing, marker, TYPETHREEFOURDISTANCE, LETTERRADIUS, double):
    A = 200
    B = (math.sqrt(200 ** 2 - LETTERRADIUS ** 2))
    C = LETTERRADIUS
    neededCosine = (B**2 + A**2 - C**2) / (2*A*B)
    neededAngle = (math.degrees(math.acos(neededCosine)))

    letterRing.forward(TYPETHREEFOURDISTANCE)
    letterRing.left(90)
    letterRing.pendown()
    letterRing.circle(LETTERRADIUS)
    if double == True:
        letterRing.penup()
        letterRing.left(90)
        letterRing.forward(20)
        letterRing.right(90)
        letterRing.pendown()
        letterRing.circle(LETTERRADIUS - 20)
    marker.left(neededAngle)
    marker.forward(200)
    marker.pendown()
    marker.forward(10)
    marker.penup()
    marker.backward(210)
    marker.right(neededAngle * 2)
    marker.forward(200)
    marker.pendown()
    marker.forward(10)

def drawTypeFour(letterRing, TYPETHREEFOURDISTANCE, LETTERRADIUS, double):
    letterRing.forward(TYPETHREEFOURDISTANCE)
    letterRing.left(90)
    letterRing.pendown()
    letterRing.circle(LETTERRADIUS)
    if double == True:
        letterRing.penup()
        letterRing.left(90)
        letterRing.forward(20)
        letterRing.right(90)
        letterRing.pendown()
        letterRing.circle(LETTERRADIUS - 20)