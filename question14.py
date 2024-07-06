# To calculate the angle between the hour and minute hands of a clock, 
from math import floor
hour=int(input("Enter hour "))
minutes=int(input("Enter minutes "))
hour=hour*30+minutes*0.5;
minutes=minutes*6;
if(minutes>hour):
 angle=floor((minutes)-(hour))
else:
 angle=floor((hour)-(minutes))
if(angle>180):
    angle=360-angle
print("Angle between hour and minute hand is",angle,"degrees")