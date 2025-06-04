#!/usr/bin/env python3
"""
Multiplication Table Generator
Generates and prints the multiplication table for a given number from 1 to 10.
"""

def main():
    # Get user input
    number = int(input("Enter a number to see its multiplication table: "))
    
    # Generate and print multiplication table
    for i in range(1, 11):
        print(f"{number} * {i} = {number * i}")

if __name__ == "__main__":
    main()
