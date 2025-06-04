#!/usr/bin/env python3

def daily_reminder():
    # Get user input
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    # Validate input
    while priority not in ['high', 'medium', 'low']:
        print("Invalid priority! Please enter high, medium, or low.")
        priority = input("Priority (high/medium/low): ").lower()

    while time_bound not in ['yes', 'no']:
        print("Please answer with yes or no.")
        time_bound = input("Is it time-bound? (yes/no): ").lower()

    # Process and generate reminder
    match priority:
        case 'high':
            if time_bound == 'yes':
                print(f"\nReminder: '{task}' is a high priority task that requires immediate attention today!")
            else:
                print(f"\nReminder: '{task}' is a high priority task. Please prioritize it today.")
        case 'medium':
            if time_bound == 'yes':
                print(f"\nReminder: '{task}' is a medium priority task that should be completed soon.")
            else:
                print(f"\nNote: '{task}' is a medium priority task. Schedule it for this week.")
        case 'low':
            if time_bound == 'yes':
                print(f"\nNote: '{task}' is a low priority task with a time constraint. Consider doing it when possible.")
            else:
                print(f"\nNote: '{task}' is a low priority task. Consider completing it when you have free time.")

if __name__ == "__main__":
    daily_reminder()
