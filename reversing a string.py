#to create the reverse of the string 
s = input("Enter :")
print(s[::-1])

#to check if a string is palindrome or not 
m = s[::-1]
if m==s:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
