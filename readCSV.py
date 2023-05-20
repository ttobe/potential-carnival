import os
import sys

with open('Data/Restaurant_Link.csv', 'r') as file:
    lines = file.read().split('\n')
name = []
link = []
for i in range(len(lines)):
    a, b =lines[i].split(',')
    name.append(a)
    link.append(b)


