#function checks if the current element is unique in its row.
#3 parameters the array, rown and column indexes of current element

def check_row_of_current_Element(grids,row,col):
    ele=grids[row][col]
    temp=grids[row][col+1:5]
    print(temp,'   ',end=" ")
    if ele in temp:
        return 1

    return 0


#function checks if the current element is unique in its column
#3 parameters the array, rown and column indexes of current element

def check_col_of_current_Element(grids,row,col):
    temp=[]
    ele=grids[row][col]
    for a in range(row+1,5):
        temp.append(grids[a][col])
    print(temp)
    if ele in temp:
        return 1
    return 0
    

#function to check if a given sudoku puzzle solution is valid (only the rowssand columns are being checked) has one parameter the array

def sudoku(grids):
    flag=0
    i=0
    j=0
    while(i<5 and flag==0):
        j=0
        while(j<5):
            flag=check_row_of_current_Element(grids,i,j)

            if(flag==1):
                break


            flag=check_col_of_current_Element(grids,i,j)

            if(flag==1):
                break
            
            j=j+1
        i=i+1

    if flag==0:
        print("True")
    else :
        print("False")





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

#function call

sudoku(grids)

