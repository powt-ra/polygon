import random
import turtle
from polygon_shape import Polygon

screen = turtle.Screen()
screen.title("Static Polygon Art")
screen.bgcolor("black")
screen.tracer(0)

polygons = []

for _ in range(20):
    polygon = Polygon(
        x=random.randint(-250, 150),
        y=random.randint(-200, 150),
        sides=random.randint(3, 7),
        side_length=random.randint(50, 130),
        color=(random.uniform(0.4, 1),
               random.uniform(0.4, 1),
               random.uniform(0.4, 1)),
        pen_size=random.randint(1, 8),
        angle=random.randint(0, 359),
    )
    polygons.append(polygon)

for polygon in polygons:
    polygon.draw()

screen.update() 
screen.mainloop()