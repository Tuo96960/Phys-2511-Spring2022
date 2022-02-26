import numpy as np
import matplotlib as mpl
from matplotlib import style
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

f = open ("Copy Lab 6 Data set.txt", "r")

# : date, time PM, state, city, airport, , , lat, long, codeame, speed, mph, codename, Peak Wind Gust,

lines = f.readlines()
#27 == len(lines)
list_1 = []
x=[]
y=[]
lat = []
long = []
city =[]
time=[]
y_array = np.array([])
c_array = np.array([])

for line in lines:
    list_1 = line.rstrip()
            #print(words)
    string = ''
    string += list_1
            #print(string)
    words = string.split(",")
            #print(words[10])
    y = words[10]
    y_array = np.append(y_array, int(y))
    lat = words[7]
            #print(lat)
    long = words[8]
    city = words[3]
    c_array = np.append(c_array, city)
    
fig = plt.figure()
fig = plt.figure(figsize=(20, 5))
fig.set_facecolor("black")
plt.bar(c_array, y_array, color='darkolivegreen')
plt.title("2/22/2019 Wind Speeds of Philadelphia and Surrounding Counties", color="w")
plt.xlabel("Counties", color="w")
plt.ylabel("Wind Speeds (mph)", color="w")
plt.figtext(0,0.01, "Wind speeds (mph) in different counties including and around Philadelphia on the day 2/19/2022.", color="w")
plt.show()

f.close()

    
    
    
    
