#write a function to find greatest between 2 numbers
def compare(a, b):
    if(a>b):
        print(a,"is greater than",b)
    elif(b>a):
        print(b,"is greater than",a)
    else:
        print("Both are equal")

x = int(input("Enter first number : "))
y = int(input("Enter second number : "))
compare(x, y)