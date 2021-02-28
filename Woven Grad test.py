# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 13:36:00 2021

@author: Ashutosh Shukla
"""
import math
import re
x, y = 0, 0

while True:
    step = input("Input your command in the format: F/B/R/L#step number: ")
    break

#To split the entire input string into a list of strings:
indstep = step.split(",")
print("The steps that you mentioned individually are:", indstep)
  
#To find individual lengths of distance traversed      
l = []
res=""
for i in indstep:
    res = (re.findall(r'(\d+)', i)[0] )
    l.append(str(res))
l = list(map(int, l))
print("The indivisual step counts of each move respectively are",l)
      
for j in indstep:           
    if re.search("F",j)
    indstep[j] == "F":
        y = y + int(l[j])
    elif indstep[j] == "B":
        y = y - int(l[j])
    elif indstep[j] == "L":
        x = x - int(l[j])
    elif indstep[j] == "R":
        x = x + int(l[j])

c = math.sqrt(x**2 + y**2)
    
print("Distance:", c)

