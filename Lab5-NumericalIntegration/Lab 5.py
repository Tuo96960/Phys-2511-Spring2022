#This imports all my functions
import numpy as np
import matplotlib.pyplot as plot
x=np.arange(-5,5,.1)

################################################

#This is my function and area
y1 = -0.5*x + 4
actual_area_y1 = 40

#These are my values
Δx = 1
n_y1=-5

#These are my arrays
n_step_y1 = np.array([n_y1])
a_y1=np.array([(-0.5*n_y1+4)])

#This is my loop to find the area based on my chosen Δx, putting the areas into an array
while n_y1<6:
    n_y1 += Δx #add Δx to points to make rectangles up to 100
    n_step_y1 = np.append (n_step_y1, n_y1) #add nstep to an array
    area_y1 = Δx * (-0.5*(n_y1) + 4) #find area for rectangle
    a_y1 = np.append (a_y1, area_y1) #add area to an array
    if n_y1 ==5:
        break  #stops loop

#This adds my areas at each point and finds the total area and percent difference from actual area
print ("The area for the function y=-0.5x+4 is", np.sum(a_y1)) #find sum of area array and print sum as area for function
perdiff = (abs(actual_area_y1 - np.sum(a_y1))/((actual_area_y1 + np.sum(a_y1))/2))*100 #make %difference equation
print ("The actual area for y=-0.5x+4 is 40. The % difference between actual value and coded value is", perdiff, "%")

###########################################################
#This is my attempt at making a percent difference vs. different n steps plot. 

#These are my values
area_graph_y1 = 0
b_y1 = -5
Δx_graph_y1 = 0

#these are my arrays
perdiff_array_y1 = ([0])
#Δx_array_y1 = (dtype=float)
a_graph_y1 = np.array([(-0.5*b_y1+4)])

#this loop goes through different Δx sizes and finds the area and percent difference of the function at each Δx, putting values into arrays
#if Δx_graph_y1 <= 5:
#    Δx_graph_y1 += 1 
#    Δx_array_y1 = np.append (Δx_array_y1, Δx_graph_y1)
#    while Δx_graph_y1 < 5:
#        b_y1 += Δx_graph_y1
#        a_graph_y1 = np.append (a_graph_y1, b_y1)
#        perdiff_graph_y1 = (abs(actual_area_y1 - np.sum(a_graph_y1))/((actual_area_y1 + np.sum(a_graph_y1))/2))*100
#        perdiff_array_y1 = np.append (perdiff_array_y1, perdiff_graph_y1)
#        if b_y1 == 5:
#            break

#This shows what is not working
#print(perdiff_array_y1)
#print(Δx_array_y1)

#This is my plotting
plot.figure()
plot.title("Percent difference v. n step size (Y1)")
plot.axis([-5,5,0,30])
plot.xlabel("n step size")
plot.ylabel("percent difference")
#plot.plot(Δx_array_y1,perdiff_array_y1)
#plot.show()

################################################
#y2 math
y2 = -0.29*x**2 - x + 12.5
actual_area_y2 = 100.83
n_y2=-5
n_step_y2 = np.array([n_y2])
a_y2=np.array([-0.29*(n_y2)**2 -(n_y2) + 12.5])
perdiff_array_y2 = np.empty(11, dtype=np.int)
while n_y2<6:
    n_y2 += Δx #add Δx to points to make rectangles up to 100
    n_step_y2 = np.append (n_step_y2, n_y2) #add nstep to an array
    area_y2 = Δx * (-0.29*(n_y2)**2 - (n_y2) + 12.5) #find area for rectangle
    a_y2 = np.append (a_y2, area_y2) #add area to an array
    if n_y2 ==5:
        break  #stops loop
print ("The area for the function y=-0.29*x**2-x+12.5 is", np.sum(a_y2))
perdiff_y2 = (abs(actual_area_y2 - np.sum(a_y2))/((actual_area_y2 + np.sum(a_y2))/2))*100
print ("The actual area for y=-0.29*x**2-x+12.5 is 100.83. The % difference between actual value and coded value is", perdiff_y2,"%")
###########################################################
#This is my attempt at making a percent difference vs. different n steps plot. 
#These are my values
area_graph_y2 = 0
b_y2 = -5
Δx_graph_y2 = 0
#these are my arrays
perdiff_array_y2 = ([0])
Δx_array_y2 = ([0])
a_graph_y2 = np.array([(-0.29*(b_y2)**2-(b_y2)+12.5)])
#this loop goes through different Δx sizes and finds the area and percent difference of the function at each Δx, putting values into arrays
#if Δx_graph_y2 <= 5:
#    Δx_graph_y2 += 1 
#    Δx_array_y2 = np.append (Δx_array_y2, Δx_graph_y2)
#    while Δx_graph_y2 < 5:
#        b_y2 += Δx_graph_y2
#        area_graph_y2 = Δx_graph_y2 = np.append (area_graph_y2, b_y2)
#        perdiff_graph_y2 = (abs(actual_area_y2 - np.sum(a_graph_y2))/((actual_area_y2 + np.sum(a_graph_y2))/2))*100
#        perdiff_array_y2 = np.append (perdiff_array_y2, perdiff_graph_y2)
#        if b_y2 == 5:
#            break

#This shows what is not working
#print(perdiff_array_y2)
#print(Δx_array_y2)

#This is my plotting
plot.figure()
plot.title("Percent difference v. n step size (Y2)")
plot.axis([-5,5,0,30])
plot.xlabel("n step size")
plot.ylabel("percent difference")
plot.plot(Δx_array_y2,perdiff_array_y2)
plot.show()

################################################
y3 = 1+((10*(x+1))*np.exp(-1*(x**2)))
actual_area_y3 = 27.72
n_y3=-5
n_step_y3 = np.array([n_y3])
a_y3=np.array([1+((10*(n_y3+1))*np.exp(-1*(n_y3**2)))])
perdiff_array_y3 = np.empty(11, dtype=np.int)
while n_y3<6:
    n_y3 += Δx #add Δx to points to make rectangles up to 100
    n_step_y3 = np.append (n_step_y3, n_y3) #add nstep to an array
    area_y3 = Δx * (1 +((10*(n_y3+1))*np.exp(-1*(n_y3**2)))) #find area for rectangle
    a_y3 = np.append (a_y3, area_y3) #add area to an array
    if n_y3 ==5:
        break  #stops loop
print ("The area for the function y=1 + ( (10 * (x + 1) ) * np.exp(-1 * (x**2) ) ) is", np.sum(a_y3))
perdiff_y3 = (abs(actual_area_y3 - np.sum(a_y3))/((actual_area_y3 + np.sum(a_y3))/2))*100
print ("The actual area for y3 = 1 + 10*(x + 1)**(-x**2) is 27.72. The % difference between actual value and coded value is", perdiff_y3, "%")
plot.clf()
###################################################################
#This is my attempt at making a percent difference vs. different n steps plot. 
#These are my values
area_graph_y3 = 0
b_y3 = -5
Δx_graph_y3 = 0
#these are my arrays
perdiff_array_y3 = ([0])
Δx_array_y3 = ([0])
a_graph_y3 = np.array([1+((10*(b_y3+1))*np.exp(-1*(b_y3**2)))])
#this loop goes through different Δx sizes and finds the area and percent difference of the function at each Δx, putting values into arrays
#if Δx_graph_y3 <= 5:
#    Δx_graph_y3 += 1 
#    Δx_array_y3 = np.append (Δx_array_y3, Δx_graph_y3)
#    while Δx_graph_y3 < 5:
#        b_y3 += Δx_graph_y3
#        area_graph_y3 = Δx_graph_y3 = np.append (area_graph_y2, b_y2)
#        perdiff_graph_y2 = (abs(actual_area_y2 - np.sum(a_graph_y2))/((actual_area_y2 + np.sum(a_graph_y2))/2))*100
#        perdiff_array_y2 = np.append (perdiff_array_y2, perdiff_graph_y2)
#        if b_y2 == 5:
#            break

#This shows what is not working
#print(perdiff_array_y2)
#print(Δx_array_y2)

#This is my plotting
plot.figure()
plot.title("Percent difference v. n step size (Y2)")
plot.axis([-5,5,0,30])
plot.xlabel("n step size")
plot.ylabel("percent difference")
plot.plot(Δx_array_y2,perdiff_array_y2)
plot.show()
