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

#Taking inputs: a string of comma-separated commands
while True:
    walk = input("Input your command in the format: F/B/R/L#distance of steps: ")
    break

#To split the entire input string into a list of strings:
walks = walk.split(",")
print("The commands that you mentioned individually are:", walks)
  
#To find individual lengths of distance traversed      
l = []
res=""
for i in walks:
    res = (re.findall(r'(\d+)', i)[0] )
    l.append(str(res))
l = list(map(int, l))
print("The indivisual step counts of each move respectively are",l)

     
for j in range(0,len(walks)):         
    if re.search("F",walks[j]):
        y = y + l[j]
    elif re.search("B",walks[j]):
        y = y - (l[j])
    elif re.search("L",walks[j]):
        x = x - (l[j])
    elif re.search("R",walks[j]):
        x = x + (l[j])       
    else:
        print("Command not recognised")

    
c = math.sqrt(x**2 + y**2)
    
print("Output:the minimum amount of distance to get back to the starting point are:", c)

