
import random as random
import math as math
import matplotlib.pyplot as mat

mat.figure()

pi = 3.14159265359
theta = int(input("Choose a degree to aim your arrow."))
theta *= pi/180  #changes degrees to radians

time = .1

velocity = 1 #initial velocity (m/s)
velocity_x = math.cos(theta)* velocity #seperates out x velocity
velocity_y = math.sin(theta)* velocity #seperates out y velocity

acceleration_y = -9.8
acceleration_x = 0
b = random.uniform(0.1, 0.15) #makes air resistance change as if wind were blowing not in a uniform fashion
m = 1
g = -9.8

arrow_x = 0 #initial arrow x coordinate
arrow_y = 20 #intital arrow y coordinate
#target = (5,10)

#sets up lists of x and y values to plot
x_values =[] 
y_values = []

while arrow_y > 0:
    arrow_x += velocity_x * time
    x_values.append(arrow_x)
    arrow_y += velocity_y * time
    y_values.append(arrow_y)
    velocity_y += acceleration_y * time
    velocity_x += acceleration_x * time
    acceleration_y -= (b/m)*velocity_y
    acceleration_x -= b * velocity_x
    time +=.1
    print(arrow_x)
    print(arrow_y)
    

if arrow_y <= 0:
    if arrow_x < 5:
        distance = 5-arrow_x
    elif arrow_x > 10:
        distance = arrow_x - 10
    else:
        distance = 0
    print ("Your arrow landed at", arrow_x, ".", "You are",  distance, "meters away from target. Try again.")



mat.plot (x_values, y_values)
mat.title ("Your Trajectory")
mat.show()

    