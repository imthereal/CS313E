#  File: Train.py

#  Description:

#  Student Name: Audrey McNay

#  Student UT EID: alm5735

#  Course Name: CS 313E

#  Unique Number: 51335

#  Date Created: 2/7/18

#  Date Last Modified: 2/13/18

import turtle

def main():
  # put label on top of page
  turtle.title ('Train')

  # setup screen size
  turtle.setup (800, 800, 0, 0)
  turtle.setworldcoordinates(0, 1302, 1302, 0)
  turtle.pensize(2)
  turtle.speed(0)

  '''
  track
  '''
  turtle.color('black')

  #bottom line
  turtle.penup()
  turtle.goto(34,919)
  turtle.pendown()
  turtle.forward(1200)

  #top line
  turtle.penup()
  turtle.goto(34,894)
  turtle.pendown()
  turtle.forward(1200)

  #track rectangles
  turtle.penup()
  turtle.goto(60,919)
  turtle.left(90)
  for i in range(12):
    turtle.pendown()
    turtle.forward(15)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(15)
    turtle.left(90)
    turtle.penup()
    turtle.forward(50)
    turtle.left(90)
  turtle.right(90)


  '''
  left side
  '''
  #main box
  turtle.penup()
  turtle.color("blue")
  turtle.goto(75, 430)
  turtle.left(180)
  turtle.pendown()
  turtle.forward(37) #small left
  turtle.left(90)
  turtle.forward(23) #small up
  turtle.left(90)
  turtle.forward(386) #small top
  turtle.left(90)
  turtle.forward(23) #small right
  turtle.left(90)
  turtle.forward(349) #small bottom (312 is total small top)
  turtle.right(90)
  turtle.forward(376) # long side
  turtle.right(90)
  turtle.forward(55)
  turtle.right(90)
  turtle.circle(101, 180)
  turtle.right(90)
  turtle.forward(55)
  turtle.right(90)
  turtle.forward(376)

  #inside
  turtle.penup()
  turtle.goto(112, 466)
  turtle.left(45)
  turtle.pendown()
  turtle.color ('blue', 'gray')
  turtle.begin_fill()
  turtle.circle (70, steps = 4)
  turtle.end_fill()
  turtle.penup()
  turtle.goto(350, 466)
  turtle.left(90)
  turtle.pendown()
  turtle.begin_fill()
  turtle.circle (70, steps = 4)
  turtle.end_fill()

  '''
  middle
  '''
  #outline
  turtle.penup()
  turtle.right(45)
  turtle.goto(387, 504)
  turtle.pendown()
  turtle.forward(665)
  turtle.left(90)
  turtle.forward(344) #370
  turtle.penup()
  turtle.goto(387, 806)
  turtle.right(90)
  turtle.pendown()
  turtle.forward(87)
  turtle.right(90)
  turtle.circle(101, 180)
  turtle.right(90)
  turtle.forward(87)
  turtle.right(90)
  turtle.circle(101, 180)
  turtle.right(90)
  turtle.forward(70)
  turtle.penup()
  turtle.left(90)
  turtle.goto(1050, 806)
  turtle.pendown()
  turtle.circle(10, steps=3)

  #inside regular lines
  turtle.penup()
  turtle.goto(387, 666) #horizontal bottom
  turtle.right(90)
  turtle.pendown()
  turtle.forward(665)
  turtle.penup()
  turtle.goto(387, 646) #horizontal top
  turtle.pendown()
  turtle.forward(665)
  turtle.penup()
  turtle.goto(565,504) # vertical left 1
  turtle.pendown()
  turtle.left(90)
  turtle.forward(142)
  turtle.penup()
  turtle.goto(585,504) # vertical left 2
  turtle.pendown()
  turtle.forward(142) 
  turtle.penup()
  turtle.goto(865,504) #vertical right 1
  turtle.pendown()
  turtle.forward(142)
  turtle.penup()
  turtle.goto(885,504) #vertical right 2
  turtle.pendown()
  turtle.forward(142)

  #inside dotted lines
  turtle.penup()
  turtle.goto(387, 652)
  turtle.right(90)
  turtle.color('black', 'black')
  for i in range (32):
    turtle.forward(20)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(3)
    turtle.end_fill()
    turtle.penup()
  turtle.goto(577, 504)
  turtle.left(90)
  for i in range(6):
    turtle.forward(20)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(3)
    turtle.end_fill()
    turtle.penup()
  turtle.goto(877, 504)
  for i in range(6):
    turtle.forward(20)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(3)
    turtle.end_fill()
    turtle.penup()

  '''
  right
  '''
  #left rectangle
  turtle.color('blue')
  turtle.goto(1052, 520)
  turtle.right(90)
  turtle.pendown()
  turtle.forward(38)
  turtle.left(90)
  turtle.forward(224)
  turtle.left(90)
  turtle.forward(38)

  #right rectangle
  turtle.penup()
  turtle.goto(1090, 600)
  turtle.right(180)
  turtle.pendown()
  turtle.forward(18)
  turtle.left(90)
  turtle.forward(104)
  turtle.left(90)
  turtle.forward(18)

  #bottom thing
  turtle.penup()
  turtle.goto(1052, 765)
  turtle.right(180)
  turtle.pendown()
  turtle.forward(76)
  turtle.left(70)
  turtle.forward(90)
  turtle.left(110)
  turtle.forward(105) #110

  #top rectangle 1
  turtle.penup()
  turtle.goto(600,504)
  turtle.left(90)
  turtle.pendown()
  turtle.forward(36)
  turtle.left(90)
  turtle.forward(94)
  turtle.left(90)
  turtle.forward(36)
  turtle.penup()
  turtle.goto(620, 468)
  turtle.pendown()
  turtle.right(180)
  turtle.forward(18)
  turtle.left(90)
  turtle.forward(54)
  turtle.left(90)
  turtle.forward(18)

  #smoke stack bottom
  turtle.penup()
  turtle.goto(844, 504)
  turtle.left(160)
  turtle.pendown()
  turtle.forward(120)
  turtle.left(110)
  turtle.forward(145)
  turtle.left(110)
  turtle.forward(120)

  #smoke stack top
  turtle.penup()
  turtle.goto(803,390)
  turtle.pendown()
  turtle.right(170)
  turtle.forward(45)
  turtle.left(60)
  turtle.forward(100)
  turtle.left(60)
  turtle.forward(45)
  
  '''
  wheels
  
  turtle.color('red')
  #wheel 1
  turtle.penup()
  turtle.settiltangle(0)
  turtle.goto(300, 765)
  turtle.pendown()
  turtle.circle(80)
  turtle.penup()
  turtle.settiltangle(0)
  turtle.goto(245, 805)
  turtle.pendown()
  turtle.circle(15)
  #TO DO: inside wheel

  #wheel 2
  turtle.penup()
  turtle.settiltangle(0)
  turtle.goto(635, 780)
  turtle.pendown()
  turtle.circle(70)
  turtle.penup()
  turtle.settiltangle(0)
  turtle.goto(585, 815)
  turtle.pendown()
  turtle.circle(10)
  #TO DO: inside wheel

  #wheel 3
  turtle.penup()
  turtle.settiltangle(0)
  turtle.goto(925, 780)
  turtle.pendown()
  turtle.circle(70)
  turtle.penup()
  turtle.settiltangle(0)
  turtle.goto(875, 815)
  turtle.pendown()
  turtle.circle(10)
  #TO DO: inside wheel
  '''

  def draw_wheels(ttl, x, y, larger_r, smaller_r):
    inc = turtle.Turtle()
    inc.speed(0)
    inc.penup()
    inc.goto(x, y + larger_r - smaller_r)

    inc.color('red')
    ttl.color('red')
    
    ttl.penup()
    ttl.setheading(0)
    
    ttl.goto(x, y)
    ttl.pendown()
    ttl.circle(larger_r)
    ttl.penup()

    spoke_angle = 5
    for r in range(2):
      for q in range(9):
        inc.goto(x, y + larger_r - smaller_r)
        inc.pendown()
        inc.circle(smaller_r, q * 45)
        ttl.goto(x, y + smaller_r)
        ttl.pendown()
        ttl.circle(larger_r - smaller_r, spoke_angle)
        ttl.goto(inc.position())
        inc.penup()
        ttl.penup()
        spoke_angle += 45
        inc.setheading(0)
        ttl.setheading(0)
      spoke_angle = -5

    inc.ht()
    ttl.ht()

  draw_wheels(turtle, 230, 725, 85, 15)
  draw_wheels(turtle, 575, 745, 75, 10)
  draw_wheels(turtle, 865, 745, 75, 10)

  # hide turtle
  turtle.hideturtle()
  

  # persist drawing
  turtle.done()

main()