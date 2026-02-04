# variables.py: Storing and using data in Python

# Creating variables (name = value)
name = "Alex"          # Text value (string). Cannot be changed in place.
age = 25               # Number value (integer). Cannot be changed in place.
scores = [90, 85, 95]  # List of numbers. Can be changed later.

# Variable names use snake_case (words separated by _)
user_score = 88
total_students = 30    # Looks like a constant (use ALL_CAPS if it never changes)

# Using variables
print(f"Name: {name}, Age: {age}")
print(f"Scores: {scores}")

# Changing a mutable object (list)
# This adds a new value inside the same list
scores.append(100)
print(f"Updated scores: {scores}")

# Reassigning a variable
# The variable now points to a completely new value
age = "twenty-five"    # Age is now text instead of a number
print(f"Age rebound: {age} (type changed dynamically)")

# Important idea
# Variables do not store values directly
# They store references (links) to values in memory
print("Variables store *references* to values.")

"""
Expected Output

Name: Alex, Age: 25
Scores: [90, 85, 95]
Updated scores: [90, 85, 95, 100]
Age rebound: twenty-five (type changed dynamically)
Variables store *references* to values.

"""