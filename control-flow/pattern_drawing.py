#!/usr/bin/env python3

 # Get the pattern size from user
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Outer while loop for rows
while row < size:
    # Inner for loop for columns
    for col in range(size):
        print("*", end="")
    
    # Move to the next line after each row
    print()
    
    # Increment row counter
    row += 1
