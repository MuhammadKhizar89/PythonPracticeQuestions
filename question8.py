# Write a program to find the euclidean distance between two coordinates.
from math import sqrt  
x1=int(input("Enter x1 "));
y1=int(input("Enter y1 "));
x2=int(input("Enter x2 "));
y2=int(input("Enter y2 "));

print ("Distance between two points is ",sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1)))