import math
import random
import time
import turtle
from polygon_shape import Polygon

screen = turtle.Screen()
screen.title("Animated Polygon Art")
screen.bgcolor("black")
screen.tracer(0)  
shapes = []
for _ in range(10):
    polygon = Polygon(
        x=0,
        y=0,
        sides=random.randint(3, 7),
        side_length=random.randint(40, 90),
        color=(random.uniform(0.4, 1),
               random.uniform(0.4, 1),
               random.uniform(0.4, 1)),
        pen_size=random.randint(2, 6),
        angle=random.randint(0, 359),
    )
    center_x = random.randint(-200, 100)
    center_y = random.randint(-150, 100)
    radius = random.randint(20, 60)
    phase = random.uniform(0, 2 * math.pi)
    shapes.append((polygon, center_x, center_y, radius, phase))

for frame in range(120):
    t = frame * 0.1 
    for polygon, cx, cy, radius, phase in shapes:
        x = cx + radius * math.cos(t + phase)
        y = cy + radius * math.sin(t + phase)
        polygon.move_to(x, y)  
    screen.update()  
    time.sleep(0.03)  

screen.mainloop()