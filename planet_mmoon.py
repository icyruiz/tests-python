import turtle
from turtle import TK
import time

def planet_and_moon():
    turtle.bgcolor("black")
    
    # Create planets
    sun = turtle.Turtle()
    sun.shape("circle")
    sun.color("yellow")
    sun.shapesize(2, 2)
    
    earth = turtle.Turtle()
    earth.shape("circle")
    earth.color("blue")
    earth.penup()
    
    moon = turtle.Turtle()
    moon.shape("circle")
    moon.color("white")
    moon.shapesize(0.5, 0.5)
    moon.penup()
    
    # Animation loop
    angle = 0
    while True:
        # Earth orbit around sun
        x = 200 * turtle.cos(turtle.radians(angle))
        y = 200 * turtle.sin(turtle.radians(angle))
        earth.goto(x, y)
        
        # Moon orbit around earth
        moon_x = x + 50 * turtle.cos(turtle.radians(angle * 5))
        moon_y = y + 50 * turtle.sin(turtle.radians(angle * 5))
        moon.goto(moon_x, moon_y)
        
        angle += 1
        time.sleep(0.01)

if __name__ == "__main__":
    planet_and_moon()
    turtle.mainloop()
