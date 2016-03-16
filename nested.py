import turtle

def nested(t, k):
     for i in range(5):
          t.left(72)
          t.forward(k)
     if k > 10:
          nested(t, k/2)


def nested2(t, k):
     for i in range(5):
          t.left(72)
          t.forward(k)
          if k > 10:
               nested2(t, k/2)

tess = turtle.Turtle()
tess.speed(100)
tess.shape("turtle")
##nested(tess,320)

tess.color("purple")
##tess.up()
##tess.goto(345,0)
##tess.down()
nested2(tess, 160)

turtle.exitonclick()
