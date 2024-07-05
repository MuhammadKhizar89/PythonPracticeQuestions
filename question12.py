# Write a program to find the volume of the cylinder. Also find the cost when ,when the cost of 1litre milk is 40Rs.
from math import pi
radius=int(input("Enter the Radius in cm "));
height=int(input("Enter the height in cm "));
volume=pi*radius*radius*height;
print(volume , " Cubic cm");
cost=int(volume)*40 ;
print(cost , " Rs")