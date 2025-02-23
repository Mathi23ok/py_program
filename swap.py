#swap two variables by using temp variable 
a = int(input("Enter a var a:"))
b = int(input("Enter a var b:"))
temp = a
a = b
b = temp
print("The variables are swapped a =",a,"b = ",b)

#without using temp variable
a,b = b,a
print(a,b)
