import turtle

# create turtle
t = turtle.Turtle()

t.shape('turtle')
t.shapesize(5, 5, 5)

t.begin_fill()
t.pensize(10)
# set colors
colors = ['red','yellow']
t.begin_fill()
for j in range(8):

    t.color(colors[j % 2])
    for i in range(18):
        t.backward(20)
        t.right(20)
    t.left(45)
t.end_fill()
colors = ['green']
t.color(colors[0])
t.left(90)
for i in range(9):
    t.forward(25)
    t.left(20)
t.forward(25)
t.left(90)
t.forward(180)

t.left(90)
for i in range(9):
    t.forward(7)
    t.left(20)
turtle.mainloop()

