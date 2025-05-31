#!/usr/bin/env python3
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
