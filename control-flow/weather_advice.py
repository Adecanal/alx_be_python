#!/usr/bin/env python3

def weather_advisor():
    # Get user input
    weather = input("What's the weather like today? (sunny/rainy/cold): ").lower()
    
    # Provide recommendations
    if weather == "sunny":
        print("Wear a t-shirt and sunglasses.")
    elif weather == "rainy":
        print("Don't forget your umbrella and a raincoat.")
    elif weather == "cold":
        print("Make sure to wear a warm coat and a scarf.")
    else:
        print("Sorry, I don't have recommendations for this weather.")

if __name__ == "__main__":
    weather_advisor()#!/usr/bin/env python3
"""
Weather Recommendation Program
"""

weather = input("What's the weather? (sunny/rainy/cold): ").lower()

if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print("Bring an umbrella and raincoat.")
elif weather == "cold":
    print("Wear a warm coat and scarf.")
else:
    print("No recommendations for this weather.")
