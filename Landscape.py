import turtle

turtle.bgcolor("light sky blue")
turtle.color("yellow")
turtle.speed(11)
turtle.penup()
turtle.left(180)
turtle.forward(235)
turtle.right(90)
turtle.forward(275)
turtle.pendown()
turtle.begin_fill()
turtle.circle(70)
turtle.end_fill()

ray = turtle.Turtle()
ray.color("green")
ray.speed(50)
ray.begin_fill()
ray.forward(400)
ray.right(90)
ray.forward(400)
ray.right(90)
ray.forward(800)
ray.right(90)
ray.forward(400)
ray.right(90)
ray.forward(400)
ray.end_fill()
ray.penup()
ray.forward(300)

joe = turtle.Turtle()
joe.color("brown")
joe.speed(50)
joe.penup()
joe.begin_fill()
joe.forward(200)
joe.pendown()
joe.left(90)
joe.forward(150)
joe.right(90)
joe.forward(30)
joe.right(90)
joe.forward(150)
joe.right(90)
joe.forward(30)
joe.end_fill()

tree = turtle.Turtle()
tree.color("Lawn Green")
tree.speed(50)
tree.penup()
tree.forward(280)
tree.left(90)
tree.forward(195)
tree.pendown()
tree.begin_fill()
tree.circle(70)
tree.end_fill()

apple = turtle.Turtle()
apple.color("red")
apple.speed(11)
apple.penup()
apple.forward(190)
apple.left(90)
apple.forward(160)
apple.pendown()
apple.begin_fill()
apple.circle(8)
apple.end_fill()
apple.penup()
apple.forward(40)
apple.right(90)
apple.forward(60)
apple.pendown()
apple.begin_fill()
apple.circle(8)
apple.end_fill()
apple.penup()
apple.forward(150)

barn = turtle.Turtle()
barn.color("red")
barn.penup()
barn.right(90)
barn.forward(100)

turtle.exitonclick()