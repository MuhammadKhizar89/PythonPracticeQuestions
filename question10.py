# Write a program that will take user input of cost price and selling price and determines whether its a loss or a profit

cost1=int(input("Enter the cost price "));
cost2=int(input("Enter the selling price "));
if(cost1<cost2):
    print("Profit");
elif(cost1>cost2):
    print("Loss");
else:
    print("Neither Profit nor Loss");