# This program prints a square pattern of stars with a given size.
n = int(input("Enter the number:"))
for i in range(n):
    for j in range(n):
        print("*", end="")
    print()

# This program prints a right-angled triangle pattern of stars with a given size.
for i in range(n):
    for j in range(i+1):
        print("*", end="")
    print()

# This program prints an inverted right-angled triangle pattern of stars with a given size.
for i in range(n):
    for j in range(n-i-1):
      print("*", end="")
    print()    

# This program prints a pyramid pattern of stars with a given size.

for i in range(n):
    for j in range(n-i-1):
        print(" ", end="")
    for k in range(2*i+1):
        print("*", end="")
    print()

# This program prints a diamond pattern of stars with a given size.

for i in range(n):
    for j in range(n-i-1):
        print(" ", end="")
    for k in range(2*i+1):
        print("*", end="")
    print()
for i in range(n-1):
    for j in range(i+1):
        print(" ", end="")
    for k in range(2*(n-i-1)-1):
        print("*", end="")
    print()

# This program prints a hollow square pattern of stars with a given size.
# The outer loop iterates through each row, and the inner loop iterates through each column.

for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()  
