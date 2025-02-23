#largest among three numbers
a = int(input("Enter a num1:"))
b = int(input("Enter a num2:"))
c = int(input("Enter a num3:"))
if (a>b and a>c):
    print(a,"is greater")
elif (b>a and b>c):
    print(b,"is greater")
elif (c>a and c>b):
    print(c,"is greater")
