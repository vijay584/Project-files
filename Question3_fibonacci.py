number=int(input("no of terms in the series (0 is not valid) = "))

if number==1:
    print("\n\n the fibonacci series is : ",end=" ")
    print(0)


elif number>=2:
    num1=0
    num2=1
    print("\n\n the fibonacci series is : ",end=" ")
    print(num1,num2,end=" ")
    number=number-2
    while(number>0):
        temp=num2
        num2=num2+num1
        num1=temp
        number=number-1
        print(num2,end=" ")


else:
    print("Enter a valid number")

