#!/usr/bin/env python3
"""
Simple Calculator with Match-Case
Performs basic arithmetic operations based on user input.
"""

def main():
    # Get user input
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Choose the operation (+, -, *, /): ")

    # Perform calculation using match-case
    match operation:
        case "+":
            result = num1 + num2
            print(f"The result is {result}")
        case "-":
            result = num1 - num2
            print(f"The result is {result}")
        case "*":
            result = num1 * num2
            print(f"The result is {result}")
        case "/":
            if num2 == 0:
                print("Cannot divide by zero.")
            else:
                result = num1 / num2
                print(f"The result is {result}")
        case _:
            print("Invalid operation. Please choose from +, -, *, /")

if __name__ == "__main__":
    main()
