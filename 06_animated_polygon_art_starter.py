"""Animated art: 10 Polygon objects moving along small circular paths."""
import math
import random
import time
import turtle
from polygon_shape import Polygon

screen = turtle.Screen()
screen.title("Animated Polygon Art")
screen.bgcolor("black")
screen.tracer(0)  # turn off automatic drawing updates

# Each item: (polygon, center x, center y, radius, starting phase)
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
    t = frame * 0.1  # the angle grows a little every frame
    for polygon, cx, cy, radius, phase in shapes:
        x = cx + radius * math.cos(t + phase)
        y = cy + radius * math.sin(t + phase)
        polygon.move_to(x, y)  # only call the method, never touch _pen
    screen.update()  # show the finished frame once
    time.sleep(0.03)  # short pause so we can see the motion

screen.mainloop()