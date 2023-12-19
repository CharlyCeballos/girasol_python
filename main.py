from turtle import *

speed(20)
bgcolor("black")
h = 0

# Dibujar el girasol
penup()
goto(0, 0)
pendown()
for i in range(16):
    for j in range(18):
        color("yellow")  # Todos los pétalos son amarillos
        h += 0.005
        rt(90)
        circle(150 - j * 6, 90)
        lt(90)
        circle(150 - j * 6, 90)
        rt(180)
    circle(40, 24)

end_fill()
done()
