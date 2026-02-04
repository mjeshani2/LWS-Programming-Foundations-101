# variables.py: Storing and using data in Python

# Assignment: Create variables
name = "Alex"  # String (immutable)
age = 25       # Integer (immutable)
scores = [90, 85, 95]  # List (mutable)

# Naming conventions: snake_case
user_score = 88
total_students = 30  # Like a constant (ALL_CAPS if truly fixed)

print(f"Name: {name}, Age: {age}")
print(f"Scores: {scores}")

# Mutability demo
scores.append(100)  # Mutates list in place
print(f"Updated scores: {scores}")

# Reassignment (creates new object)
age = "twenty-five"  # Now string!
print(f"Age rebound: {age} (type changed dynamically)")

# Check memory (conceptual—use id() in interactive shell)
print("Variables store *references* to values.")

"""
Expected Output

Name: Alex, Age: 25
Scores: [90, 85, 95]
Updated scores: [90, 85, 95, 100]
Age rebound: twenty-five (type changed dynamically)
Variables store *references* to values.

"""