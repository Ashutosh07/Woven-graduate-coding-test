# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 09:36:00 2021

@author: Ashutosh Shukla
"""
import math
x, y = 0, 0

while True:
    step = input("Input your command in the format: F/B/R/L#step number: ")

    if step == "":
        break

    else:
        step = step.split(" ")

        if step[0] == "UP":
            y = y + int(step[1])
        elif step[0] == "DOWN":
            y = y - int(step[1])
        elif step[0] == "LEFT":
            x = x - int(step[1])
        elif step[0] == "RIGHT":
            x = x + int(step[1])

c = math.sqrt(x**2 + y**2)

print("Distance:", c)
