# Write a program that take a user inputr of three angles and will find out whether it can form a triangle or not.

user1=int(input("Enter the first angle "));
user2=int(input("Enter the second angle "));
user3=int(input("Enter the third angle "));
if(user1+user2+user3==180):
    print("It can form a triangle");
else:
    print("It can't form a triangle")