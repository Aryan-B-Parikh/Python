# python_learning_demo.py
"""
A small multi-feature Python program for learning.
Covers: variables, input, functions, loops, lists, and dictionaries.
"""

# 1. Variables & Printing
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"\n👋 Hello {name}, you are {age} years old.")

# 2. Conditional Statements
if age < 18:
    print("You are a minor.")
elif 18 <= age < 60:
    print("You are an adult.")
else:
    print("You are a senior citizen.")

# 3. Lists & Loops
hobbies = []
print("\nEnter 3 hobbies:")
for i in range(3):
    hobby = input(f"Hobby {i+1}: ")
    hobbies.append(hobby)

print("\nYour hobbies are:")
for hobby in hobbies:
    print(f"- {hobby}")

# 4. Dictionary & Functions
def calculate_bmi(weight, height):
    """Calculate and return BMI given weight(kg) and height(m)."""
    return weight / (height ** 2)

print("\nLet's calculate your BMI!")
weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))
bmi = calculate_bmi(weight, height)

bmi_categories = {
    "Underweight": bmi < 18.5,
    "Normal": 18.5 <= bmi < 24.9,
    "Overweight": 25 <= bmi < 29.9,
    "Obese": bmi >= 30
}

for category, condition in bmi_categories.items():
    if condition:
        print(f"Your BMI is {bmi:.2f} → {category}")
        break

print("\n✅ End of demo. Thanks for running this!")
