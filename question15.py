# find if the given two rectangles overlap or not
L1=(0,10)
R1=(10,0)
L2=(5,5)
R2=(15,0)
rec1=((L1[0],L1[1]),(R1[0],L1[1]),(L1[0],R1[1]),(R1[0],R1[1]));
rec2=((L2[0],L2[1]),(R2[0],L2[1]),(L2[0],R2[1]),(R2[0],R2[1]));
print(rec1,rec2)
if((rec2[0][0]<=rec1[1][0] and rec2[3][1]<=rec1[0][1]and rec2[1][0]>=rec1[0][0] and rec2[0][1]>=rec1[3][1])):
    print("Overlappng");
else:
    print("Not OverLapping");