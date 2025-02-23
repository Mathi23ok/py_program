n = int(input("Enter a number:"))
if n>1:
    for i in range(2,(n//2)+1):
        if n%i==0:
            print("Not a prime")
            break
    else:
        print("It is a prime ")
