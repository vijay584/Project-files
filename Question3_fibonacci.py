number=int(input("no of terms in the series (0 is not valid) = "))

def fibonacci(number):
    if number<=1:
        return number
    else:
        return fibonacci(number-2)+fibonacci(number-1)


if number<0:
    print(invalid)

else:
    for i in range(0,number):
        result=fibonacci(i)
        print(result,end=" ")



