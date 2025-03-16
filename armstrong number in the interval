n = int(input("Enter the lower limit :"))
m = int(input("Enter the upper limit :"))
for num in range(n,m+1):
    original = num #creating a copy of the number
    sum = 0 
    d = len(str(num)) #finding the number of digits
    while original > 0: #loop to find the sum of the digits raised to the power of the number of digits
        digit = original % 10 #to get the last digit
        sum += digit ** d #adding the sum of the digits raised to the power of the number of digits
        original //= 10 #to remove the last digit
        if num == sum: #if the sum is equal to num then it is an armstrong number
            print(num)
            break
