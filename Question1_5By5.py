#grids=[[5,5,3,4,2],[2,4,5,3,1],[3,1,4,2,5],[5,2,3,5,4],[4,5,2,1,3]]

#if manually entering array replace the below grids list to the one above and comment the code within block

grids=[]


#----------------------Block-----------------------------------#
############ takes each row as input from user can be commented if needed
print("Input format : Enter a row with a space between each element and press enter") 
for i in range(0,5):
    print("ENter row ",i+1)
    a=input()
    l=a.split()
    for j in range(0,5):
        l[j]=int(l[j])
    grids.append(l)

#---------------------Block-----------------------------------#



flag=0
i=0
j=0
while(i<5 and flag==0):
    while(j<5):
        ele=grids[i][j]
        temp=grids[i][j+1:5]
        print(temp,'   ',end=" ")
        if ele in temp:
            flag=1
            break
        temp=[]
        for a in range(i+1,5):
            temp.append(grids[a][j])
        print(temp)
        if ele in temp:
            flag=1
            break
        j=j+1
    i=i+1

if flag==0:
    print("True")
else :
    print("False")
        
        
    
    
