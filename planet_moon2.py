#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import math

fig, ax = plt.subplots()
ax.set_xlim(-300, 300)
ax.set_ylim(-300, 300)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Create celestial bodies
sun = plt.Circle((0, 0), 20, color='yellow')
earth = plt.Circle((200, 0), 10, color='blue')
moon = plt.Circle((220, 0), 5, color='white')

ax.add_patch(sun)
ax.add_patch(earth)
ax.add_patch(moon)

def animate(frame):
    # Earth orbit
    earth_angle = math.radians(frame)
    earth_x = 200 * math.cos(earth_angle)
    earth_y = 200 * math.sin(earth_angle)
    earth.center = (earth_x, earth_y)
    
    # Moon orbit (faster)
    moon_angle = math.radians(frame * 5)
    moon_x = earth_x + 40 * math.cos(moon_angle)
    moon_y = earth_y + 40 * math.sin(moon_angle)
    moon.center = (moon_x, moon_y)
    
    return earth, moon

ani = FuncAnimation(fig, animate, frames=360, interval=20, blit=True)
plt.show()
