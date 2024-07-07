# Write a program that will determine weather when the value of temperature and humidity is provided by the user.
# TEMPERATURE(C)      HUMIDITY(%)      WEATHER

#       >= 30                             >=90                Hot and Humid
#       >= 30                             < 90                 Hot
#       <30                                >= 90               Cool and Humid
#       <30                                 <90                 Cool


temp=int(input("Enter temperature "))
hum=int(input("Enter humidity "))
if(temp>=30 and hum>=90):
    print("Hot and Humid");
elif(temp>=30 and hum<90):
    print("Hot");
elif(temp<30 and hum>=90):
    print("Cool and Humid");
elif(temp<30 and hum<90):
    print("Cool")