# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 18:41:56 2022

@author: nelso
"""
import numpy as np

# ticks = (0.1,0.2,0.3,0.4,0.5)
def finddistance(cords):
     ex = cords[0]
     ey = cords[1]
     d = np.sqrt(((ex)**2)+((ey)**2))
     return d
 
#was in code 
ds = []
for y in np.arange(0,.5, step=.01):
    d = finddistance([.5, y])
    ds.append(d/2)
print(np.mean(ds))

#added values
averagein,averageout= 9,0
d = .2027
passed = 0

while passed != 100:#loop start
    
   xay = np.zeros((100,2))#= [x,y] 
   xay = np.random.uniform(0,0.5,size = (200,2)) #,np.random.uniform(0,0.5,100)
    #print(x,y)
    
   d2center = []
   d2edge = []
   outside = 0
   inside= 0
   for i in range(200):
        #print(np.sqrt(x[i]**2+y[j]**2))
       if np.sqrt(xay[i][0]**2+xay[i][1]**2) <= d  :
            inside+=1
            d2center.append(finddistance(xay[i]))
       else:
            d2edge.append(min(.5-xay[i][0],.5-xay[i][1]))
   print(np.mean(d2center))
   averagein =np.mean(d2center)
   print(np.mean(d2edge))
   averageout =np.mean(d2edge)
   
   if abs(averagein - averageout)< 0.0001:
        passed = 100
        break
   elif averagein< averageout:
        d+=.000001
   elif averagein > averageout:
        d-=.000001
        
   print("shit it failed")
   print(f"d is now {d}")
   
   
"""
import numpy as np

ticks = (0.1,0.2,0.3,0.4,0.5)

def finddistance(cords):
    ex = cords[0]
    ey = cords[1]
    d = np.sqrt(((ex)**2)+((ey)**2))
    return d

ds = []

for y in np.arange(0,.5, step=.01):
    d = finddistance([.5, y])
    ds.append(d/2)
    
print(np.mean(ds))

xay = np.zeros((100,2))#= [x,y] 
xay = np.random.uniform(0,0.5,size = (200,2)) #,np.random.uniform(0,0.5,100)
#print(x,y)

d2center = []
d2edge = []
outside = 0
inside= 0
for i in range(200):
        #print(np.sqrt(x[i]**2+y[j]**2))
        if np.sqrt(xay[i][0]**2+xay[i][1]**2) <= .2829  :
            inside+=1
            d2center.append(finddistance(xay[i]))
        else:
            d2edge.append(min(.5-xay[i][0],.5-xay[i][1]))
print(np.mean(d2center))
print(np.mean(d2edge))

"""


"""
rmin = .1
rmax=.5

if averagein > averageout:
    
elif averagein< averageout:
    
else:
"""















"""ds = finddistance(d2center[0,:], d2center[1,:])
print(inside)
"""