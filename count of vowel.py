#count the number of vowel in the string 
s = input("Enter :").strip()
l = "AEIOUaeiou"
c = 0
for i in s:
    if i in l:
        c +=1
print("The number of vowel in string is ",c)        
