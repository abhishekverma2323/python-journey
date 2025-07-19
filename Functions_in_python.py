print("Using functions in python")

#taking user input and checking which number is greater
def check_greater(a,b,c):
    if (a>b):
        if(a>c):
            print(a,"is the greater number")
        else:
            print(c,"is the greater number")
            
    elif (b>a):
        if(b>c):
            print(b,"is the greater number")
        else:
            print(c,"is the greater number")
    
    elif (c>b):
        if(c>a):
            print(c,"is the greater number")
        else:
            print(a,"is the greater number")

x=int(input("Enter the first number: "))
y=int(input("Enter the second number: "))
z=int(input("Enter the third number: "))
print()
check_greater(x, y, z)
print("Thanks for using Python have fun!!")