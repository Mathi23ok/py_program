n = int(input("Enter a number :"))
s = 1
if n==0 or n==1:
    print("1")
if n>0:
    for i in range(1,n+1):
        s *=i
print(s)        
