import turtle
wn = turtle.Screen()
wn.bgcolor("blue")
wn.title("18 sided shape")

richie = turtle.Turtle()
richie.color("red")
richie.pensize(6) 

for _ in range(18):

    richie.forward(40)
    richie.left(20)
  
wn.mainloop
