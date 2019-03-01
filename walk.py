import turtle

# create turtle
t = turtle.Turtle()

# set colors
colors = ['red', 'blue']
oldv=0
newv=1
tmpv=0
for j in range(10):
    t.color(colors[j % 2])
    tmp = newv
    newv += oldv
    oldv = tmp
    for i in range(15):
        t.forward(newv)
        t.left(6)

turtle.mainloop()

