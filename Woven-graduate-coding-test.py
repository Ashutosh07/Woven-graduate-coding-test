# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 13:36:00 2021

Finished on Sun Feb 28 15:57:00 2021
@author: Ashutosh Shukla

For Submission Purposes for Woven-graduate-coding-test
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

     
for j in range(0,len(indstep)):         
    if re.search("F",indstep[j]):
        y = y + l[j]
    elif re.search("B",indstep[j]):
        y = y - (l[j])
    elif re.search("L",indstep[j]):
        x = x - (l[j])
    elif re.search("R",indstep[j]):
        x = x + (l[j])       
    else:
        print("Command not recognised")

    
c = math.sqrt(x**2 + y**2)
    
print("Distance:", c)

