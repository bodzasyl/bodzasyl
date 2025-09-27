import turtle
ablak = turtle.Screen()
ablak.bgcolor("lightblue")
ablak.title("Ötszög rajzolása turtle-el")
rajzolo = turtle.Turtle()
rajzolo.pensize(3)
rajzolo.color("green")
for _ in range(5):
    rajzolo.forward(100)
    rajzolo.right(72)
ablak.exitonclick()