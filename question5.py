# Write a program that will reverse a four digit number.Also it checks whether the reverse is true.

# a="abcd"
# print(a[0:3:2]);
# means hr dusra element skip hoga 

user1=input("Enter the number ");
if(user1.__len__()!=4):
    print("Number Should be 4 digit");
elif(user1[::-1]==user1):
    print("Reverse is true ",);
else:
    print("Reverse is false ");
