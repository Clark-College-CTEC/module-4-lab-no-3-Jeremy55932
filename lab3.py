# Lab No. 3
# CTEC 121
# Jeremy Lo

from graphics import *

def snowman():
    # create the graphics window
    win = GraphWin('Lab 3 - Snowman',800,800)
    
    # your code to draw the snowman goes here
    # draw three circles for the body
    # name the three circles circle1, circle2 and circl3
    
    arm = Line(Point(318,294),Point(480,294))
    arm.draw(win)

    circle1 = Circle(Point(400,400),80)
    circle1.setFill("white")
    circle1.draw(win)
    circle2 = Circle(Point(400,300),50)
    circle2.setFill("white")
    circle2.draw(win)
    circle3 = Circle(Point(400,250),40)
    circle3.setFill("white")
    circle3.draw(win)

    # draw two eyes on the top circle
    # name the two eyes using variables eye1 and eye2
    eyes1 = Circle(Point(385,234),8)
    eyes1.draw(win)

    eyes2 = eyes1.clone()
    eyes2.move(30,0) 
    eyes2.draw(win)


    # draw a nose using the polygon method and make it orange
    # name the nose using the variable nose
    nose = Polygon(Point(402,252),Point(425,258),Point(402,263))
    nose.setFill("orange")
    nose.draw(win)


    # draw a hat using a rectangle and fill it with black
    # name the hat using the variable hat
    hat = Rectangle(Point(371,215),Point(430,197))
    hat.setFill("black")
    hat.draw(win)

    # draw a line to represent the rim of the hat using a line
    # name the line using the variable hatline
    hatline = Line(Point(350,215),Point(450,215))
    hatline.draw(win)

    win.getMouse()
    print(win.getMouse())

    

    # close the program
    input('Press enter to quit the program ')
    # close the graphics window
    win.close()


# Call the snowman() function to start the program
snowman()